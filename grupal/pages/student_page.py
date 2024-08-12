import reflex as rx
from reflex import Style


@rx.page(
    route="/students",
    title="Estudiantes",
)
def students_page() -> rx.Component:
    students = [
        {"first_name": "Juan Pablo", "last_name": "Pérez Esquivel", "paralelo": "A",
         "subjects": ["Matemáticas", "Inglés", "Ciencia"]},
        {"first_name": "Maria Jose", "last_name": "López Wilson", "paralelo": "B",
         "subjects": ["Matemáticas", "Historia", "Arte"]},
        {"first_name": "Michael Smith", "last_name": "Johnson Miller", "paralelo": "C",
         "subjects": ["Matemáticas", "Ciencia", "Geografía"]},
        {"first_name": "Emily Davis", "last_name": "Davis Christian", "paralelo": "D",
         "subjects": ["Matemáticas", "Inglés", "Ciencia"]},
        {"first_name": "David Wilson", "last_name": "Wilson Perez", "paralelo": "E",
         "subjects": ["Matemáticas", "Historia", "Arte"]},
    ]

    def student_card(first_name, last_name, paralelo, subjects):
        return rx.card(
            rx.vstack(
                rx.text(f"{first_name}", font_weight="semibold", font_size="lg"),
                rx.text(f"{last_name}", color="gray.500", font_size="sm"),
                rx.text(f"Paralelo: {paralelo}", color="gray.500", font_size="sm"),
                rx.vstack(
                    rx.spacer(height="1"),
                    *[rx.badge(subject, font_size="sm", padding="2", mr="2") for subject in
                      subjects],
                    spacing="1",
                ),
            ),
            padding="6",
            border_radius="lg",
            background="rgba(0, 0, 0, 0.2)",
            box_shadow="lg",
            width="300px",
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
            rx.input(placeholder="Buscar cursos y paralelos", width="80%", padding="0.5em", margin_right="1em"),
            rx.button("Buscar", color="#2B2B2B", background_color="white", border_radius="0.3em", padding="0.5em 1em"),
            display="flex",
            justify_content="center",
            margin_top="2em"
        ),
        rx.spacer(height="2"),
        rx.flex(
            *[student_card(**student) for student in students],
            spacing="4",
            width="100%",
            padding="8",
            align_items="center",
            justify_content="center",
        ),
        style=Style(
            padding="1em",
            width="100%",
            height="100%",
            background="linear-gradient(180deg, #003366, #00143C)",
        )
    )
