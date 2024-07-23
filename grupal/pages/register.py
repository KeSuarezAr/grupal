import reflex as rx

from grupal.views.auth.register_form import register_form


@rx.page(
    route="/register",
    title="Registrarse",
)
def register_page() -> rx.Component:
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.heading("Registrarse", size="5"),
        register_form(),
        direction="column",
        gap="1rem",
    )
