import reflex as rx

from grupal.models.usuarios import UsuarioModel


def tabla_usuarios(usuarios: list[UsuarioModel]) -> rx.Component:
    return rx.table.root(
        rx.table.header(
            rx.table.row(
                rx.table.column_header_cell("Cedula"),
                rx.table.column_header_cell("Nombres"),
                rx.table.column_header_cell("Apellidos"),
                rx.table.column_header_cell("Correo"),
                rx.table.column_header_cell("Telefono"),
                rx.table.column_header_cell("Direccion"),
            ),
        ),
        rx.table.body(
            rx.foreach(usuarios, lambda usuario: row_table(usuario)),
        ),
    )


def row_table(usuario: UsuarioModel) -> rx.Component:
    return rx.table.row(
        rx.table.cell(usuario.cedula),
        rx.table.cell(usuario.nombres),
        rx.table.cell(usuario.apellidos),
        rx.table.cell(usuario.correo),
        rx.table.cell(usuario.telefono),
        rx.table.cell(usuario.direccion),
        rx.table.cell(
            rx.hstack(
                rx.button(
                    "Editar",
                    on_click=rx.redirect(
                        f"/editar_usuario/{usuario.id}/",
                    ),
                ),
                rx.button("Eliminar"),
            )
        ),
    )
