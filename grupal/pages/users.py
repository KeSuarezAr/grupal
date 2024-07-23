from typing import Optional

import reflex as rx

from grupal.connection.users import select_all, insert_admin_user, insert_profesor_user, insert_parent_user, \
    insert_student_user
from grupal.models.user import UserModel
from grupal.views.user.add_user import admin_dialogue, profesor_dialogue, parent_dialogue, student_dialogue
from grupal.views.user.users_list import users_table


class UsersState(rx.State):
    users: list[UserModel] = []
    role_filter: Optional[str] = None

    new_user: dict = {
        "name": "",
        "email": "",
        "password": "",
    }

    def get_data(self):
        self.users = select_all(self.role_filter)

    def set_role_filter(self, role):
        self.role_filter = role
        self.get_data()

    def set_username(self, username):
        self.new_user["username"] = username

    def set_email(self, email):
        self.new_user["email"] = email

    def set_password(self, password):
        self.new_user["password"] = password

    def add_admin(self):
        insert_admin_user(self.new_user)
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
            admin_dialogue(
                set_username_callback=UsersState.set_username,
                set_email_callback=UsersState.set_email,
                set_password_callback=UsersState.set_password,
                add_user_callback=UsersState.add_admin
            ),
            profesor_dialogue(
                set_username_callback=UsersState.set_username,
                set_email_callback=UsersState.set_email,
                set_password_callback=UsersState.set_password,
                add_user_callback=UsersState.add_profesor
            ),
            parent_dialogue(
                set_username_callback=UsersState.set_username,
                set_email_callback=UsersState.set_email,
                set_password_callback=UsersState.set_password,
                add_user_callback=UsersState.add_parent
            ),
            student_dialogue(
                set_username_callback=UsersState.set_username,
                set_email_callback=UsersState.set_email,
                set_password_callback=UsersState.set_password,
                add_user_callback=UsersState.add_student
            ),
            rx.select.root(
                rx.select.trigger(
                    placeholder="Seleccione un Rol",
                ),
                rx.select.content(
                    rx.select.group(
                        rx.select.item(
                            "Admin", value="admin"
                        ),
                        rx.select.item(
                            "Profesor", value="profesor"
                        ),
                        rx.select.item(
                            "Padre", value="parent"
                        ),
                        rx.select.item(
                            "Estudiante", value="student"
                        ),
                    ),
                ),
                on_change=UsersState.set_role_filter,
            ),
            direction="row",
        ),
        users_table(UsersState.users),
        direction="column",
    )
