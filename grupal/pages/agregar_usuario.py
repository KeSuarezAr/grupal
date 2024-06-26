import reflex as rx

from grupal.connection.usuarios import insert_usuario


class AddFormState(rx.State):
    form_data: dict = {}

    def handle_submit(self, form_data: dict):
        self.form_data = form_data
        insert_usuario(form_data)
        rx.redirect("/usuarios")


@rx.page("/agregar_usuario", title="agregar usuario")
def agregar_usuario_page() -> rx.Component:
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.heading("Nuevo Usuario", size="9"),
        rx.form(
            rx.vstack(
                rx.input(
                    placeholder="Cedula",
                    name="cedula",
                    type="number",
                ),
                rx.input(
                    placeholder="nombres",
                    name="nombres",
                ),
                rx.input(
                    placeholder="apellidos",
                    name="apellidos",
                ),
                rx.input(
                    placeholder="correo",
                    name="correo",
                ),
                rx.input(
                    placeholder="direccion",
                    name="direccion",
                ),
                rx.input(
                    placeholder="telefono",
                    name="telefono",
                    type="number",
                ),
                rx.select(["admin", "profesor", "estudiante"], name="rol"),
                rx.button("Submit", type="submit"),
                rx.button("Cancelar"),
            ),
            on_submit=AddFormState.handle_submit,
        ),
    )
