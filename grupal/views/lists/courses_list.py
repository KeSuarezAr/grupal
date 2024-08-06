import reflex as rx

from grupal.models.course import CourseModel
from grupal.styles.index_styles import curso_card_style


def courses_list(courses: list[CourseModel]) -> rx.Component:
    return rx.box(
        rx.foreach(
            courses,
            course_card
        ),
    )


def course_card(course: CourseModel) -> rx.Component:
    return rx.box(
        rx.image(src="/mnt/data/image.png", width="100%", height="auto", border_radius="0.5em"),
        rx.text(course.name, font_size="1.2em", color="white", text_align="center"),
        rx.text(course.paralelo, font_size="1em", color="white", text_align="center"),
        style=curso_card_style
    )
