import reflex as rx

from grupal.connection.auth import login_user


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
            on_click=LoginFormState.submit,
        ),
        reset_on_submit=True,
        justify="center",
        align="center",

    )
