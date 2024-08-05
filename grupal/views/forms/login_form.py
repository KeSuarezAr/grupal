import reflex as rx

from grupal.states.forms.login_form import LoginFormState


def login_form(
) -> rx.Component:
    return rx.form(
        rx.input(
            placeholder="Email",
            name="email",
            type="text",
            input_mode="text",
            on_change=LoginFormState.set_email,
        ),
        rx.input(
            placeholder="Contraseña",
            name="password",
            type="password",
            input_mode="text",
            on_change=LoginFormState.set_password,
        ),
        rx.button(
            "Guardar",
            type="submit",
            on_click=LoginFormState.login,
        ),
        reset_on_submit=True,
        justify="center",
        align="center",

    )
