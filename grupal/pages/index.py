import reflex as rx

from grupal.components.sidebar import build_sidebar


@rx.page("/")
def index_page() -> rx.Component:
    border_width = 3

    return rx.container(
        rx.color_mode.button(position="bottom-right"),
        rx.hstack(
            build_sidebar(["Proyecto 1", "Proyecto 2", "Proyecto 3"]),
            build_body(),
            width=f"calc(100vw - {border_width * 2}px)",
            spacing="0",
        ),
        padding="0px",
        display="flex",
        flex_direction="row",
        border=f"{border_width}px solid black",
        border_radius="50px",
        height="100vh",
        width="100vw",
        overflow="hidden",
    )


def build_body() -> rx.Component:
    return rx.container(
        rx.hstack(
            rx.vstack(
                rx.image(
                    src="./favicon.ico",
                    width="240px",
                    height="auto",
                    border_radius="15px 50px",
                    border="5px solid #C5C5C5",
                ),
                rx.text("Kevin Andres Suarez Armijos"),
                rx.text("Fecha Entrega: 09 Jun"),
            ),
            rx.vstack(
                rx.text_field(placeholder="Completar mi Libro"),
                rx.text_field(placeholder="Descripcion", height="35 vh"),
            ),
            height="80vh",
            width="90vw",
            padding="20px",
            border="2px solid #555",
            border_radius="15px 50px",
        ),
        height="100vh",
        background_color="lightgray",
        flex_grow=3,
    )
