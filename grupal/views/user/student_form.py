import reflex as rx


def trigger_body(title: str) -> rx.Component:
    return rx.dialog.trigger(
        rx.button(f"Añadir {title} ", width="150px"),
    )


def content_body(title: str, add_user_callback: callable) -> rx.Component:
    return rx.dialog.content(
        rx.dialog.title(f"Añadir Usuario {title}"),
        student_form(add_user_callback),
        style={"width": "400px", "padding": "10px"},
    )


def student_dialogue(
        add_user_callback: callable,
) -> rx.Component:
    return rx.dialog.root(
        trigger_body("Estudiante"),
        content_body("Estudiante", add_user_callback),
    )


class StudentFormState(rx.State):
    new_user: dict = {
        "username": "",
        "email": "",
        "password": "",
    }

    def set_username(self, username):
        self.new_user["username"] = username

    def set_email(self, email):
        self.new_user["email"] = email

    def set_password(self, password):
        self.new_user["password"] = password


def student_form(
        add_product_callback: callable,
) -> rx.Component:
    return rx.form(
        rx.input(
            placeholder="Nombre de Usuario",
            name="username",
            type="text",
            input_mode="text",
            on_change=StudentFormState.set_username,
        ),
        rx.input(
            placeholder="Email",
            name="email",
            type="text",
            input_mode="text",
            on_change=StudentFormState.set_email,
        ),
        rx.input(
            placeholder="Contraseña",
            name="password",
            type="password",
            input_mode="text",
            on_change=StudentFormState.set_password,
        ),
        rx.button(
            "Guardar",
            type="submit",
            on_click=add_product_callback(StudentFormState.new_user),
        ),
        rx.dialog.close(
            rx.button("Cancelar", variant="soft", color_scheme="red"),
        ),
        reset_on_submit=True,
        justify="center",
        align="center",

    )