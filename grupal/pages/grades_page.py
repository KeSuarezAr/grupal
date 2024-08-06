import reflex as rx

from grupal.states.models.course import CourseState

from grupal.styles.index_styles import *
from grupal.styles.styles import page_style

from grupal.views.forms.course_form import course_dialogue
from grupal.views.lists.courses_list import courses_list


@rx.page(
    on_load=CourseState.get_courses,
    route="/",
    title="Inicio",
)
def grades_page() -> rx.Component:
    return rx.container(
        course_dialogue(),
        courses_list(),
        rx.color_mode.button(position="absolute", top="1em", right="1em"),
        style=page_style
    )
