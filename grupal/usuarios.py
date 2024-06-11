import reflex as rx


@rx.page("/usuarios")
def usuarios_page() -> rx.Component:
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.heading("Usuarios", size="9"),
        rx.container(
            rx.hstack(
                rx.button("Nuevo Usuario", on_click=rx.redirect("/agregar_usuario")),
                justify="center",
            ),
            spacing="5",
            justify="center",
        ),
    )
