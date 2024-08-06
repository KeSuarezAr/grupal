import reflex as rx

@rx.page(
    route="/dashboard",
    title="Dashboard",
)
def dashboard_page() -> rx.Component:
    sidebar_items = [
        {"label": "Cursos", "active": True},
        {"label": "Horarios", "active": True},
        {"label": "Calificaciones", "active": True},
        {"label": "Actividades", "active": True},
    ]
    
    def sidebar_item(item):
        return rx.box(
            rx.text(item["label"], font_size="1.2em", color="white", padding="1em"),
            background="#1E3A5F" if not item["active"] else "#48CAE4",
            width="100%",
            margin_bottom="1em",
            cursor="pointer",
        )
    
    content_items = [
        {"title": "2do A", "description": "Traer plastilina"},
        {"title": "3ro B", "description": "Dibujar las plantas"},
        {"title": "4to C", "description": "Traer algo para compartir"},
        {"title": "5to A", "description": "Resolver los ejercicios de matemáticas"},    ]
    
    def content_card(item):
        return rx.box(
            rx.text(item["title"], font_size="1.2em", color="white", text_align="center"),
            rx.text(item["description"], font_size="1em", color="white", text_align="center"),
            width="200px",
            height="200px",
            margin="1em",
            padding="1em",
            background="#2A5D7C",
            border_radius="0.5em",
            box_shadow="0 4px 8px rgba(0, 0, 0, 0.15)",
            display="flex",
            flex_direction="column",
            justify_content="center",
            align_items="center",
            aspect_ratio="1 / 1",
            # min_width="150px",
            # min_height="150px",
        )
    
    return rx.box(
        rx.box(
            *[sidebar_item(item) for item in sidebar_items],
            width="20%",
            background="#2A5D7C",
            padding="2em",
            box_shadow="2px 0 5px rgba(0,0,0,0.1)"
        ),
        rx.box(
            *[content_card(item) for item in content_items],
            display="flex",
            justify_content="center",
            flex_wrap="wrap",
            width="80%",
            padding="2em",
            background="linear-gradient(to bottom right, navy, red)",
        ),
        display="flex",
        width="100%",
        height="100vh",
        background="linear-gradient(to bottom right, navy, red)",
    )

# Código adicional para iniciar la aplicación Reflex
if __name__ == "__main__":
    rx.run(dashboard_page)
