import reflex as rx


@rx.page(
    route="/actividades",
    title="Actividades de Clase",
)
def actividades_page() -> rx.Component:
    # Datos para la barra lateral
    sidebar_items = [
        {"label": "Cursos", "active": False},
        {"label": "Horarios", "active": False},
        {"label": "Calificaciones", "active": False},
        {"label": "Actividades", "active": True},
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

    # Datos para las actividades
    activities = [
        {"title": "Matemáticas", "description": "Resolver los ejercicios de la página 42"},
        {"title": "Historia", "description": "Leer el capítulo 5 y responder las preguntas"},
        {"title": "Ciencias", "description": "Preparar una presentación sobre el ciclo del agua"},
        {"title": "Inglés", "description": "Escribir un ensayo sobre tu libro favorito"},
    ]

    # Función para renderizar cada tarjeta de actividad
    def activity_card(activity):
        return rx.box(
            rx.text(activity["title"], font_size="1.5em", color="white", text_align="center"),
            rx.text(activity["description"], font_size="1.2em", color="white", text_align="center"),
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
            *[activity_card(activity) for activity in activities],
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
    app.add_page(actividades_page)
    app.compile()
