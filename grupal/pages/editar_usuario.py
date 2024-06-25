import reflex as rx

from grupal.models.usuarios import UsuarioModel

from grupal.connection.usuarios import insert_usuario, select_user, update_usuario


class EditFormState(rx.State):
    form_data: list[UsuarioModel] = []

    def get_data(self):
        id: str = self.router.page.params.get("id")
        self.form_data: list[UsuarioModel] = select_user(id)
        print(self.form_data[0].cedula)

    def handle_submit(self, form_data: dict):
        id: str = self.router.page.params.get("id")
        self.form_data = form_data
        update_usuario(id, form_data)
        rx.redirect("/usuarios")


@rx.page(
    route="/editar_usuario/[id]",
    title="editar usuario",
    on_load=EditFormState.get_data,
)
def editar_usuario_page() -> rx.Component:
    usuario: UsuarioModel = EditFormState.form_data[0]
    print(usuario)
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.heading("Editar Usuario", size="9"),
        rx.form(
            rx.vstack(
                rx.input(
                    placeholder="Cedula",
                    name="cedula",
                    type="number",
                    # value=EditFormState.form_data[0].cedula,
                ),
                rx.input(
                    placeholder="Nombres",
                    name="nombres",
                ),
                rx.input(
                    placeholder="Apellidos",
                    name="apellidos",
                ),
                rx.input(
                    placeholder="Correo",
                    name="correo",
                ),
                rx.input(
                    placeholder="Direccion",
                    name="direccion",
                ),
                rx.input(
                    placeholder="Telefono",
                    name="telefono",
                    type="number",
                ),
                rx.select(
                    ["admin", "profesor", "estudiante"],
                    name="rol",
                ),
                rx.button("Submit", type="submit"),
                rx.button("Cancelar", on_click=rx.redirect("/usuarios")),
            ),
            on_submit=EditFormState.handle_submit,
            reset_on_submit=True,
        ),
    )
