from typing import Optional

import reflex as rx

from grupal.connection.users import select_all, insert_admin_user, insert_profesor_user, insert_parent_user, \
    insert_student_user
from grupal.models.user import UserModel
from grupal.views.user.admin_form import admin_dialogue
from grupal.views.user.parent_form import parent_dialogue
from grupal.views.user.profesor_form import profesor_dialogue
from grupal.views.user.student_form import student_dialogue
from grupal.views.user.users_list import users_table


def select_role(on_change: callable) -> rx.Component:
    return rx.select.root(
        rx.select.trigger(),
        rx.select.content(
            rx.select.group(
                rx.select.item("Todos", value=None),
                rx.select.item("Admin", value="admin"),
                rx.select.item("Profesor", value="profesor"),
                rx.select.item("Padre", value="parent"),
                rx.select.item("Estudiante", value="student"),
            ),
        ),
        on_change=on_change,
    )


class UsersState(rx.State):
    users: list[UserModel] = []
    role_filter: Optional[str] = None

    def get_data(self):
        self.users = select_all(self.role_filter)

    def set_role_filter(self, role):
        self.role_filter = role
        self.get_data()

    def add_admin(self, form_data: dict):
        insert_admin_user(form_data)
        self.get_data()

    def add_profesor(self):
        insert_profesor_user(self.new_user)
        self.get_data()

    def add_parent(self):
        insert_parent_user(self.new_user)
        self.get_data()

    def add_student(self):
        insert_student_user(self.new_user)
        self.get_data()


@rx.page(
    on_load=UsersState.get_data,
    route="/users",
    title="Users",
)
def users_page() -> rx.Component:
    return rx.flex(
        rx.color_mode.button(position="top-right"),
        rx.heading("Usuarios", size="5"),
        rx.flex(
            admin_dialogue(add_user_callback=UsersState.add_admin),
            profesor_dialogue(add_user_callback=UsersState.add_profesor),
            parent_dialogue(add_user_callback=UsersState.add_parent),
            student_dialogue(add_user_callback=UsersState.add_student),
            select_role(on_change=UsersState.set_role_filter),
            direction="row",
            gap="1rem",
        ),
        users_table(UsersState.users),
        direction="column",
        gap="1rem",
    )
