import reflex as rx
from reflex import Style

from grupal.states.forms.course_form import CourseFormState


def content_body(title: str) -> rx.Component:
    return rx.dialog.content(
        rx.dialog.title(f"Añadir Usuario {title}"),
        course_form(),
        style={"width": "400px", "padding": "10px"},
    )


def trigger_body(title: str) -> rx.Component:
    return rx.dialog.trigger(
        rx.box(
            rx.button(f"Añadir {title} ", width="150px"), display="flex", justify_content="center", padding="0.5em"
        ),
    )


def course_dialogue() -> rx.Component:
    return rx.dialog.root(
        trigger_body("Curso"),
        content_body("Curso"),
    )


def course_form() -> rx.Component:
    return rx.form(
        rx.input(
            placeholder="Nombre",
            name="name",
            type="text",
            input_mode="text",
            on_change=CourseFormState.set_name,
        ),
        rx.input(
            placeholder="Paralelo",
            name="paralelo",
            type="text",
            input_mode="text",
            on_change=CourseFormState.set_paralelo,
        ),
        rx.button(
            "Guardar",
            type="submit",
            on_click=CourseFormState.add_course,
        ),
        rx.dialog.close(
            rx.button("Cancelar", variant="soft", color_scheme="red"),
        ),
        reset_on_submit=True,
        justify="center",
        align="center",

    )
