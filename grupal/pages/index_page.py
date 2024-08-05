import reflex as rx


@rx.page(
    route="/",
    title="Inicio",
)
def index_page() -> rx.Component:
    return rx.container(
        rx.color_mode.button(position="bottom-right"),
        rx.heading(
            "Bienvenido al Sistema de Administración de Calificaciones",
            size="5",
            center=True,
        ),
    )
