import reflex as rx

from grupal.models.trimester import TrimesterModel


def trimesters_table(trimesters: list[TrimesterModel]) -> rx.Component:
    return rx.table.root(
        rx.table.header(
            rx.table.row(
                rx.table.column_header_cell("Nombre"),
                rx.table.column_header_cell("Descripción"),
                rx.table.column_header_cell("Actions"),
            ),
        ),
        rx.table.body(
            rx.foreach(
                trimesters,
                trimester_row
            ),
        ),
    )


def trimester_row(trimester: TrimesterModel) -> rx.Component:
    return rx.table.row(
        rx.table.cell(trimester.name),
        rx.table.cell(trimester.description),
        rx.table.cell(
            rx.hstack(
                rx.button(
                    "Edit",
                    # on_click=lambda: State.edit_user(lists.id),
                ),
                rx.button(
                    "Delete",
                    # on_click=lambda: UserState.delete_user(user.id),
                )
            ),
        ),
    )
