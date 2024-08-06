import reflex as rx

from grupal.states.models.course import CourseState
from grupal.styles.index_styles import *
from grupal.views.forms.course_form import course_dialogue
from grupal.views.lists.courses_list import courses_list


@rx.page(
    on_load=CourseState.get_courses,
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
        {"nombre": "Curso 7", "paralelo": "Paralelo H"},
        {"nombre": "Curso 8", "paralelo": "Paralelo I"},
        {"nombre": "Curso 9", "paralelo": "Paralelo J"},
    ]

    def header_box():
        return rx.box(
            rx.hstack(
                rx.text("Bienvenido a nuestra institución", style=text_style),
                rx.image(src="/escuela.jpeg", style=image_style),
                style=box_style
            ),
            style=header_style
        )

    def search_box():
        return rx.box(
            rx.input(placeholder="Buscar cursos y paralelos", width="80%", padding="0.5em", margin_right="1em"),
            rx.button("Buscar", color="black", background_color="white", border_radius="0.3em", padding="0.5em 1em"),
            display="flex",
            justify_content="center",
            margin_top="2em"
        ),

    def login_button():
        return rx.button(
            "Iniciar Sesión",
            on_click=rx.redirect("/login"),
            style=login_button_style,
        ),

    return rx.container(
        header_box(),
        course_dialogue(),
        search_box(),
        courses_list(CourseState.courses),
        login_button(),
        rx.color_mode.button(position="absolute", top="1em", right="1em"),
        style=index_page_style
    )
