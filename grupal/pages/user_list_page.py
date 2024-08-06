import reflex as rx

from grupal.states.models.user import UserState
from grupal.views.forms.admin_form import admin_dialogue
from grupal.views.forms.parent_form import parent_dialogue
from grupal.views.forms.teacher_form import teacher_dialogue
from grupal.views.forms.student_form import student_dialogue
from grupal.views.lists.users_list import users_table


# def select_role() -> rx.Component:
#     return rx.select.root(
#         rx.select.trigger(),
#         rx.select.content(
#             rx.select.group(
#                 rx.select.item("Todos", value=None),
#                 rx.select.item("Admin", value="admin"),
#                 rx.select.item("Profesor", value="profesor"),
#                 rx.select.item("Padre", value="parent"),
#                 rx.select.item("Estudiante", value="student"),
#             ),
#         ),
#         on_change=UserListState.set_list_filter,
#     )


@rx.page(
    on_load=UserState.get_users,
    route="/users",
    title="Users",
)
def users_page() -> rx.Component:
    return rx.flex(
        rx.color_mode.button(position="top-right"),
        rx.heading("Usuarios", size="5"),
        rx.flex(
            admin_dialogue(),
            teacher_dialogue(),
            parent_dialogue(),
            student_dialogue(),
            # select_role(),
            direction="row",
            gap="1rem",
        ),
        users_table(UserState.users),
        direction="column",
        gap="1rem",
    )
