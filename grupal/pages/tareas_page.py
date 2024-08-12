import reflex as rx
from reflex import Style


@rx.page(
    route="/tareas",
    title="Tareas",
)
def tareas_page() -> rx.Component:
    tasks = [
        ["Tarea de Matemáticas", "Tarea", "15 Abr, 2023", "16 Abr, 2023"],
        ["Presentación en Inglés", "Presentación", "12 Abr, 2023", "14 Abr, 2023"],
        ["Proyecto de Ciencia", "Proyecto", "10 Abr, 2023", "12 Abr, 2023"],
    ]
    grades = [
        ["Tarea de Matemáticas", "Tarea", "16 Abr, 2023", "A"],
        ["Presentación en Inglés", "Presentación", "14 Abr, 2023", "B+"],
        ["Proyecto de Ciencia", "Proyecto", "12 Abr, 2023", "A-"],
    ]

    def create_card(name, secondary_text, metadata):
        return rx.box(
            rx.card(
                rx.vstack(
                    rx.text(name, font_weight="semibold", font_size="lg"),
                    *[
                        rx.text(f"{key}: {value}", color="gray.500", font_size="sm")
                        for key, value in metadata.items()
                    ],
                    rx.text(secondary_text, color="gray.500", font_size="sm"),
                ),
                padding="6",
                border_radius="lg",
                background="rgba(0, 0, 0, 0.2)",
                box_shadow="lg",
            ),
            width="30%",
            margin_bottom="4",
        )

    def task_card(name, category, created, modified):
        metadata = {"Created": created, "Modified": modified}
        return create_card(name, category, metadata)

    def grade_card(name, category, date, grade):
        metadata = {"Date": date, "Grade": grade}
        return create_card(name, category, metadata)

    return rx.container(
        rx.box(
            rx.hstack(
                rx.text(
                    "Bienvenido a nuestra institución",
                    font_size="3em",
                    color="white",
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
            background="linear-gradient(180deg, #003366, #00143C)",
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
        rx.heading("Tareas"),
        rx.flex(
            *[
                task_card(t[0], t[1], t[2], t[3])
                for t in tasks
            ],
            spacing="4",
            flex_wrap="wrap",
            width="100%",
        ),
        rx.heading("Calificaciones"),
        rx.flex(
            *[
                grade_card(g[0], g[1], g[2], g[3])
                for g in grades
            ],
            spacing="4",
            wrap="wrap",
            width="100%",
        ),
        style=Style(
            padding="1em",
            width="100%",
            height="100%",
            background="linear-gradient(180deg, #003366, #00143C)",
        )
    )
