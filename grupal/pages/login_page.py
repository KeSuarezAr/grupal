import reflex as rx

from grupal.styles.login_styles import login_page_style
from grupal.components.auth.login_form import login_form


@rx.page(
    route="/login",
    title="Login",
)
def login_page() -> rx.Component:
    return rx.container(
        rx.center(
            login_form(),
        ),
        style=login_page_style,
    )
