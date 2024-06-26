import reflex as rx

from grupal.models.usuarios import UsuarioModel

from grupal.connection.usuarios import select_user, update_usuario


class EditFormState(rx.State):
    form_data: dict = {}

    def handle_submit(self, form_data: dict):
        update_usuario(form_data.get("id"), form_data)
        rx.redirect("/usuarios")


def dialog_editar_usuario(usuario: UsuarioModel) -> rx.Component:
    return rx.dialog.root(
        rx.dialog.trigger(
            rx.button("Editar"),
        ),
        rx.dialog.content(
            rx.flex(
                rx.dialog.title("Editar usuario"),
                usuario_form(usuario),
                justify="center",
                align="center",
                direction="column",
            ),
            style={"width": "400px", "padding": "10px"},
        ),
    )


def usuario_form(usuario: UsuarioModel) -> rx.Component:
    return rx.form(
        rx.input(
            placeholder="Cedula",
            name="cedula",
            type="number",
            default_value=usuario.cedula,
        ),
        rx.input(
            placeholder="nombres",
            name="nombres",
            default_value=usuario.nombres,
        ),
        rx.input(
            placeholder="apellidos",
            name="apellidos",
            default_value=usuario.apellidos,
        ),
        rx.input(
            placeholder="correo",
            name="correo",
            default_value=usuario.correo,
        ),
        rx.input(
            placeholder="direccion",
            name="direccion",
            default_value=usuario.direccion,
        ),
        rx.input(
            placeholder="telefono",
            name="telefono",
            default_value=usuario.telefono,
        ),
        rx.select(
            name="rol",
            items=["admin", "profesor", "estudiante"],
            default_value=usuario.rol,
        ),
        rx.dialog.close(
            rx.flex(
                rx.button("Cancelar", variant="soft", color_scheme="red"),
                rx.button("Guardar", type="submit"),
                spacing="2",
                direction="column",
            )
        ),
        on_submit=EditFormState.handle_submit,
        justify="center",
        align="center",
    )
