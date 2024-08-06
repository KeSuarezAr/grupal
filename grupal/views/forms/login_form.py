import reflex as rx

from grupal.states.forms.login_form import LoginFormState
from grupal.styles.login_styles import form_style, form_item_style


def login_form(
) -> rx.Component:
    return rx.form(
        rx.input(
            placeholder="Email",
            name="email",
            type="text",
            input_mode="text",
            on_change=LoginFormState.set_email,
            style=form_item_style
        ),
        rx.input(
            placeholder="Contraseña",
            name="password",
            type="password",
            input_mode="text",
            on_change=LoginFormState.set_password,
            style=form_item_style
        ),
        rx.button(
            "Guardar",
            type="submit",
            on_click=LoginFormState.login,
        ),
        reset_on_submit=True,
        style=form_style
    )
