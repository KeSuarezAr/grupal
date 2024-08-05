import reflex as rx

from grupal.views.forms.login_form import login_form


@rx.page(
    route="/login",
    title="Login",
)
def login_page() -> rx.Component:
    return rx.container(
        rx.color_mode.button(position="top-right"),
        rx.heading("Login", size="5"),
        login_form(),
        direction="column",
        gap="1rem",
    )
