import reflex as rx

from grupal.models.person import PersonModel
from grupal.models.user import UserModel


def users_table(users: list[UserModel]) -> rx.Component:
    return rx.table.root(
        rx.table.header(
            rx.table.row(
                rx.table.column_header_cell("Nombre de Usuario"),
                rx.table.column_header_cell("Correo"),
                rx.table.column_header_cell("Contraseña"),
                rx.table.column_header_cell("Rol"),
                rx.table.column_header_cell("Informacion"),
                rx.table.column_header_cell("Acciones"),
            ),
        ),
        rx.table.body(
            rx.foreach(users, lambda user: user_row(user)),
        ),
    )


def user_row(user: UserModel) -> rx.Component:
    return rx.table.row(
        rx.table.cell(user.username),
        rx.table.cell(user.email),
        rx.table.cell(user.password),
        rx.table.cell(user.role),
        person_row(user.person),
        actions_row(user),
    )


def person_row(person: PersonModel) -> rx.Component:
    return rx.table.cell(
        rx.vstack(
            rx.text(f"{person.first_name} - {person.last_name}"),
            rx.text(person.cedula),
            rx.text(person.address),
        )
    )


def actions_row(user: UserModel) -> rx.Component:
    return rx.table.cell(
        rx.vstack(
            # edit_user_dialog(user),
            rx.button("Eliminar"),
        )
    )
