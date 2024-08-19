import reflex as rx


@rx.page(
    route="/calificaciones",
    title="Calificaciones del Estudiante",
)
def calificaciones_page() -> rx.Component:
    # Datos para la barra lateral
    sidebar_items = [
        {"label": "Cursos", "active": False},
        {"label": "Horarios", "active": False},
        {"label": "Calificaciones", "active": True},
        {"label": "Actividades", "active": False},
    ]

    # Función para renderizar cada ítem de la barra lateral
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

    # Datos para las calificaciones
    grades = {
        "Matemáticas": "A",
        "Historia": "B+",
        "Ciencias": "A-",
        "Inglés": "B",
    }

    # Función para renderizar cada tarjeta de calificación
    def grade_card(subject, grade):
        return rx.box(
            rx.text(subject, font_size="1.5em", color="white", text_align="center"),
            rx.text(f"Calificación: {grade}", font_size="1.2em", color="white", text_align="center"),
            width="250px",
            height="150px",
            margin="1em",
            padding="1.5em",
            background="linear-gradient(135deg, #3A6073 0%, #16222A 100%)",
            border_radius="15px",
            box_shadow="0 10px 15px rgba(0, 0, 0, 0.2)",
            display="flex",
            flex_direction="column",
            justify_content="center",
            align_items="center",
            transition="transform 0.3s",
            _hover={
                "transform": "translateY(-10px)",
            },
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
            *[grade_card(subject, grade) for subject, grade in grades.items()],
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
    app.add_page(calificaciones_page)
    app.compile()
