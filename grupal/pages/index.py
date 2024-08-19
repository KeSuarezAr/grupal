import reflex as rx


@rx.page(
    route="/",
    title="Inicio",
)
def index_page() -> rx.Component:
    cursos = [
        {"nombre": "Curso 1", "paralelo": "Paralelo A"},
        {"nombre": "Curso 2", "paralelo": "Paralelo B"},
        {"nombre": "Curso 3", "paralelo": "Paralelo C"},
        {"nombre": "Curso 4", "paralelo": "Paralelo D"},
        {"nombre": "Curso 5", "paralelo": "Paralelo F"},
        {"nombre": "Curso 6", "paralelo": "Paralelo G"},
    ]

    def curso_card(curso):
        return rx.box(
            rx.text(curso["nombre"], font_size="1.2em", color="#2B2B2B", text_align="center"),
            rx.text(curso["paralelo"], font_size="1em", color="#2B2B2B", text_align="center"),
            width="200px",
            margin="1em",
            padding="1em",
            background="rgba(255, 255, 255, 0.8)",
            border_radius="0.5em",
            box_shadow="0 4px 8px rgba(0, 0, 0, 0.15)"
        )

    return rx.container(
        rx.box(
            rx.hstack(
                rx.text(
                    "Bienvenido a nuestra institución",
                    font_size="3em",
                    color="#2B2B2B",
                    text_align="center",
                    font_family="'Helvetica Neue', Arial, sans-serif",
                    flex="1"
                ),
                rx.image(
                    src="/escuelajpeg.jpeg",
                    width="50%",
                    height="auto",
                    border_radius="0.5em"
                ),
                width="100%",
                align_items="center",
                justify_content="space-between"
            ),
            width="70%",
            margin="auto",
            padding="3em",
            background="linear-gradient(180deg, #8ABAD3 0%, #FFB3B3 100%)",
            border_radius="0.5em",
            box_shadow="0 4px 8px rgba(0, 0, 0, 0.15)"
        ),
        rx.box(
            rx.input(placeholder="Buscar Estudiantes", width="80%", padding="0.5em", margin_right="1em"),
            rx.button("Buscar", color="#2B2B2B", background_color="white", border_radius="0.3em", padding="0.5em 1em"),
            display="flex",
            justify_content="center",
            margin_top="2em"
        ),
        rx.box(
            *[curso_card(curso) for curso in cursos],
            display="flex",
            justify_content="center",
            flex_wrap="wrap",
            margin_top="2em"
        ),
        rx.button(
            "Iniciar Sesión",
            color="white",
            background_color="#6A9BCF",
            hover_background_color="#88B7E6",
            border_radius="0.3em",
            padding="1em",
            position="absolute",
            top="1em",
            left="1em",
            on_click=lambda: rx.redirect("/login")
        ),
        rx.color_mode.button(position="absolute", top="1em", right="1em"),
        width="100%",
        height="100vh",
        background="linear-gradient(180deg, #8ABAD3 0%, #FFB3B3 100%)",
        display="flex",
        flex_direction="column",
        align_items="center"
    )
