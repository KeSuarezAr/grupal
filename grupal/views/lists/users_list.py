import reflex as rx

from grupal.models.person import PersonModel
from grupal.models.user import UserModel
from grupal.states.models.user import UserState


def users_table(users: list[UserModel]) -> rx.Component:
    return rx.table.root(
        rx.table.header(
            rx.table.row(
                rx.table.column_header_cell("Nombre de Usuario"),
                rx.table.column_header_cell("Correo"),
                rx.table.column_header_cell("Rol"),
                rx.table.column_header_cell("Informacion"),
                rx.table.column_header_cell("Actions"),
            ),
        ),
        rx.table.body(
            rx.foreach(
                users,
                user_row
            ),
        ),
    )


def user_row(user: UserModel) -> rx.Component:
    return rx.table.row(
        rx.table.cell(user.username),
        rx.table.cell(user.email),
        rx.table.cell(user.role),
        person_cell(user.person),
        rx.table.cell(
            rx.hstack(
                rx.button(
                    "Edit",
                    # on_click=lambda: State.edit_user(lists.id),
                ),
                rx.button(
                    "Delete",
                    on_click=lambda: UserState.delete_user(user.id),
                )
            ),
        ),
    )


def person_cell(person: PersonModel) -> rx.Component:
    return rx.table.cell(
        rx.vstack(
            rx.text(f"{person.first_name} {person.last_name}", font_weight="bold"),
            rx.text(f"Cedula: {person.cedula}"),
            rx.text(f"Direccion: {person.address}"),
            align_items="start",
            spacing="1",
        )
    )
