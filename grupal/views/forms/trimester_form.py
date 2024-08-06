import reflex as rx

from grupal.states.forms.admin_form import AdminFormState
from grupal.states.forms.trimestre_form import TrimestreFormState


def content_body() -> rx.Component:
    return rx.dialog.content(
        rx.dialog.title(f"Añadir Trimestre"),
        trimester_form(),
        style={"width": "400px", "padding": "10px"},
    )


def trigger_body() -> rx.Component:
    return rx.dialog.trigger(
        rx.button(f"Añadir Trimestre", width="150px"),
    )


def trimester_dialogue() -> rx.Component:
    return rx.dialog.root(
        trigger_body(),
        content_body(),
    )


def trimester_form() -> rx.Component:
    return rx.form(
        rx.input(
            placeholder="Nombre",
            name="name",
            type="text",
            input_mode="text",
            on_change=TrimestreFormState.set_name,
        ),
        rx.input(
            placeholder="Descripcion",
            name="description",
            type="text",
            input_mode="text",
            on_change=TrimestreFormState.set_description,
        ),
        rx.button(
            "Guardar",
            type="submit",
            on_click=TrimestreFormState.add_trimester,
        ),
        rx.dialog.close(
            rx.button("Cancelar", variant="soft", color_scheme="red"),
        ),
        reset_on_submit=True,
        justify="center",
        align="center",

    )
