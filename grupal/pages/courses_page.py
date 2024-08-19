import reflex as rx

from grupal.components.forms.course_form import course_dialogue
from grupal.components.lists.courses_list import courses_list
from grupal.states.models.course import CourseState
from grupal.styles.index_styles import *
from grupal.styles.styles import page_style


@rx.page(
    on_load=CourseState.get_courses,
    route="/courses",
    title="Cursos",
)
def courses_page() -> rx.Component:
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
            style=search_box_style,
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
        courses_list(),
        login_button(),
        rx.color_mode.button(position="absolute", top="1em", right="1em"),
        style=page_style
    )
