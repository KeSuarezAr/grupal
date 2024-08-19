import reflex as rx


@rx.page(
    route="/horario",
    title="Horario del Estudiante",
)
def horario_page() -> rx.Component:
    sidebar_items = [
        {"label": "Cursos", "active": False},
        {"label": "Horarios", "active": True},
        {"label": "Calificaciones", "active": False},
        {"label": "Actividades", "active": False},
    ]

    def sidebar_item(item):
        return rx.box(
            rx.text(
                item["label"],
                font_size="1.2em",
                color="white",
                font_weight="bold",
                padding="1em"
            ),
            background="#2A3B4C" if not item["active"] else "#48CAE4",
            border_radius="10px",
            margin_bottom="1em",
            cursor="pointer",
            transition="background 0.3s, transform 0.3s",
            _hover={
                "background": "#48CAE4",
                "transform": "scale(1.05)",
            },
        )

    # Datos para el horario
    schedule = {
        "Lunes": [("Matemáticas", "9:00 AM - 10:30 AM"), ("Ciencias", "11:00 AM - 12:30 PM")],
        "Martes": [("Historia", "9:00 AM - 10:30 AM"), ("Inglés", "11:00 AM - 12:30 PM")],
        "Miércoles": [("Matemáticas", "9:00 AM - 10:30 AM"), ("Ciencias", "11:00 AM - 12:30 PM")],
        "Jueves": [("Historia", "9:00 AM - 10:30 AM"), ("Inglés", "11:00 AM - 12:30 PM")],
        "Viernes": [("Matemáticas", "9:00 AM - 10:30 AM"), ("Ciencias", "11:00 AM - 12:30 PM")],
    }

    # Función para renderizar cada columna de horario
    def schedule_column(day, classes):
        return rx.box(
            rx.text(day, font_size="1.5em", color="white", text_align="center", margin_bottom="1em"),
            *[
                rx.box(
                    rx.text(subject, font_size="1.2em", color="white", font_weight="bold"),
                    rx.text(time, font_size="1em", color="white"),
                    padding="1em",
                    background="linear-gradient(135deg, #3A6073 0%, #16222A 100%)",
                    border_radius="10px",
                    box_shadow="0 10px 15px rgba(0, 0, 0, 0.2)",
                    margin_bottom="1em",
                    text_align="center",
                    display="flex",
                    flex_direction="column",
                    justify_content="center",
                    align_items="center",
                    transition="transform 0.3s",
                    _hover={
                        "transform": "translateY(-10px)",
                    },
                )
                for subject, time in classes
            ],
            width="180px",
            padding="1em",
            background="#1A2B3C",
            border_radius="15px",
            margin="1em",
        )

    # Composición de la página
    return rx.box(
        rx.box(
            *[sidebar_item(item) for item in sidebar_items],
            width="20%",
            background="#1A2B3C",
            padding="2em",
            box_shadow="2px 0 10px rgba(0, 0, 0, 0.15)",
            border_radius="15px",
        ),
        rx.box(
            *[schedule_column(day, classes) for day, classes in schedule.items()],
            display="flex",
            justify_content="center",
            flex_wrap="wrap",
            width="80%",
            padding="2em",
            background="linear-gradient(to bottom right, #000428, #004e92)",
            border_radius="15px",
        ),
        display="flex",
        width="100%",
        height="100vh",
        padding="2em",
        background="#1E1E1E",
    )


# Código adicional para iniciar la aplicación Reflex
if __name__ == "__main__":
    app = rx.App()
    app.add_page(horario_page)
    app.compile()
