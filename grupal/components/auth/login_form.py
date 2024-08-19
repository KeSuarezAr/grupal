import reflex as rx
from grupal.connection.auth import login_user
from grupal.styles.login_styles import *


class LoginFormState(rx.State):
    user: dict = {
        "email": "",
        "password": "",
    }

    def submit(self):
        res = login_user(self.user)

        if res:
            print("Login correcto")
        else:
            print("Login incorrecto")

    def set_email(self, email):
        self.user["email"] = email

    def set_password(self, password):
        self.user["password"] = password


def login_form() -> rx.Component:
    return rx.card(
        rx.vstack(
            rx.center(
                rx.image(
                    src="/escuelajpeg.jpeg",
                    style=login_image_style
                ),
                rx.heading(
                    "Unidad Educativa Padre Julian Lorente",
                    style=login_heading_style
                ),
                direction="column", spacing="5", style=login_header_style,
            ),
            rx.vstack(
                rx.text(
                    "Correo Electronico",
                    weight="medium", size="3", style=login_input_label_style
                ),
                rx.input(
                    placeholder="ejemplo@gmail.com",
                    type="email",
                    size="3", style=login_input_style,
                ),
                spacing="2",
                style=login_input_container_style
            ),
            rx.vstack(
                rx.hstack(
                    rx.text(
                        "Contraseña",
                        size="3", weight="medium", style=login_input_label_style
                    ),
                    rx.link(
                        "Olvidaste tu contraseña?",
                        size="3", style=login_input_label_style
                    ),
                    justify="between", width="100%",
                ),
                rx.input(
                    placeholder="Contraseña",
                    type="password",
                    size="3", style=login_input_style,
                ),
                style=login_input_container_style
            ),
            rx.button("Sign in", size="3", width="100%"),
            rx.center(
                rx.text("Nuevo usuario?", size="3"),
                rx.link("Sign up", href="#", size="3"),
                direction="row", spacing="2", style=signin_button_style,
            ),
            spacing="6",
            style=login_body_style,
        ),
        style=login_card_style,
    )
