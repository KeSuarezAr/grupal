import reflex as rx

from grupal.states.forms.profesor_form import ProfesorFormState


def content_body(title: str) -> rx.Component:
    return rx.dialog.content(
        rx.dialog.title(f"Añadir Usuario {title}"),
        teacher_form(),
        style={"width": "400px", "padding": "10px"},
    )


def trigger_body(title: str) -> rx.Component:
    return rx.dialog.trigger(
        rx.button(f"Añadir {title} ", width="150px"),
    )


def teacher_dialogue() -> rx.Component:
    return rx.dialog.root(
        trigger_body("Profesor"),
        content_body("Profesor"),
    )


def teacher_form() -> rx.Component:
    return rx.form(
        rx.input(
            placeholder="Nombre de Usuario",
            name="username",
            type="text",
            input_mode="text",
            on_change=ProfesorFormState.set_username,
        ),
        rx.input(
            placeholder="Email",
            name="email",
            type="text",
            input_mode="text",
            on_change=ProfesorFormState.set_email,
        ),
        rx.input(
            placeholder="Contraseña",
            name="password",
            type="password",
            input_mode="text",
            on_change=ProfesorFormState.set_password,
        ),
        rx.input(
            placeholder="Nombres",
            name="first_name",
            type="text",
            input_mode="text",
            on_change=ProfesorFormState.set_first_name,
        ),
        rx.input(
            placeholder="Apellidos",
            name="last_name",
            type="text",
            input_mode="text",
            on_change=ProfesorFormState.set_last_name,
        ),
        rx.input(
            placeholder="Cedula",
            name="cedula",
            type="text",
            input_mode="text",
            on_change=ProfesorFormState.set_cedula,
        ),
        rx.input(
            placeholder="Dirección",
            name="address",
            type="text",
            input_mode="text",
            on_change=ProfesorFormState.set_address,
        ),
        rx.button(
            "Guardar",
            type="submit",
            on_click=ProfesorFormState.add_profesor,
        ),
        rx.dialog.close(
            rx.button("Cancelar", variant="soft", color_scheme="red"),
        ),
        reset_on_submit=True,
        justify="center",
        align="center",
    )
