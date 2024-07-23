import reflex as rx

from grupal.connection.auth import register_user


class RegisterFormState(rx.State):
    user: dict = {
        "username": "",
        "email": "",
        "password": "",
    }

    def submit(self):
        register_user(self.user)

    def set_username(self, username):
        self.user["username"] = username

    def set_email(self, email):
        self.user["email"] = email

    def set_password(self, password):
        self.user["password"] = password


def register_form() -> rx.Component:
    return rx.form(
        rx.input(
            placeholder="Nombre de Usuario",
            name="username",
            type="text",
            input_mode="text",
            on_change=RegisterFormState.set_username,
        ),
        rx.input(
            placeholder="Email",
            name="email",
            type="text",
            input_mode="text",
            on_change=RegisterFormState.set_email,
        ),
        rx.input(
            placeholder="Contraseña",
            name="password",
            type="password",
            input_mode="text",
            on_change=RegisterFormState.set_password,
        ),
        rx.button(
            "Guardar",
            type="submit",
            on_click=RegisterFormState.submit,
        ),
        reset_on_submit=True,
        justify="center",
        align="center",

    )
