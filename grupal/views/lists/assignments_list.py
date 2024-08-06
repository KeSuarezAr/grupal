import reflex as rx

from grupal.models.assignment import AssignmentModel


def asignaciones_table(asignaciones: list[AssignmentModel]) -> rx.Component:
    return rx.table.root(
        rx.table.header(
            rx.table.row(
                rx.table.column_header_cell("Nombre"),
                rx.table.column_header_cell("Trimestre ID"),
                rx.table.column_header_cell("Categoria"),
                rx.table.column_header_cell("Fecha de Creacion"),
                rx.table.column_header_cell("Fecha de Modificacion"),
            ),
        ),
        rx.table.body(
            rx.foreach(
                asignaciones,
                assignment_row
            ),
        ),
    )


def assignment_row(assignment: AssignmentModel) -> rx.Component:
    return rx.table.row(
        rx.table.cell(assignment.name),
        rx.table.cell(assignment.category),
        # rx.table.cell(assignment.fecha_creacion),
        # rx.table.cell(assignment.fecha_modificacion),
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
