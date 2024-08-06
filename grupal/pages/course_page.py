import reflex as rx

from grupal.states.models.course import CourseState

from grupal.styles.index_styles import *
from grupal.styles.styles import page_style

from grupal.views.forms.course_form import course_dialogue
from grupal.views.lists.courses_list import courses_list


@rx.page(
    route="/",
    title="Inicio",
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

    return rx.container(
        header_box(),
        course_dialogue(),
        courses_list(),
        rx.color_mode.button(position="absolute", top="1em", right="1em"),
        style=page_style
    )
