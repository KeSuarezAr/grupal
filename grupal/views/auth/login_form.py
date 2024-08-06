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
    return rx.center(
        rx.card(
            rx.vstack(
                rx.center(
                    rx.image(
                        src="/escuelajpeg.jpeg",
                        width="8em",
                        height="auto",
                        border_radius="30px 50px",
                        border="5px solid #555"
                    ),
                    rx.heading(
                        "Unidad Educativa Padre Julian Lorente",
                        size="6",
                        as_="h2",
                        text_align="center",
                        width="100%",
                    ),
                    direction="column",
                    spacing="5",
                    width="100%"
                ),
                rx.vstack(
                    rx.text(
                        "Correo Electronico",
                        size="3",
                        weight="medium",
                        text_align="left",
                        width="100%",
                    ),
                    rx.input(
                        placeholder="ejemplo@gmail.com",
                        type="email",
                        size="3",
                        width="100%",
                    ),
                    justify="start",
                    spacing="2",
                    width="100%",
                ),
                rx.vstack(
                    rx.hstack(
                        rx.text(
                            "Contraseña",
                            size="3",
                            weight="medium",
                        ),
                        rx.link(
                            "Olvidaste tu contraseña?",
                            href="#",
                            size="3",
                        ),
                        justify="between",
                        width="100%",
                    ),
                    rx.input(
                        placeholder="Contraseña",
                        type="password",
                        size="3",
                        width="100%",
                    ),
                    spacing="2",
                    width="100%",
                ),
                rx.button("Sign in", size="3", width="100%"),
                rx.center(
                    rx.text("Nuevo usuario?", size="3"),
                    rx.link("Sign up", href="#", size="3"),
                    opacity="0.8",
                    spacing="2",
                    direction="row"
                ),
                spacing="6",
                width="100%",
            ),
            size="4",
            max_width="28em",
            width="100%",
            background_image="linear-gradient(to bottom right, navy, red)",
            padding="2em",
            border_radius="0.5em",
            box_shadow="0 4px 8px 0 rgba(0, 0, 0, 0.2)",
        ),
        height="100vh",  # To center it vertically
        background_image="linear-gradient(to bottom right, navy, red)",
    )
