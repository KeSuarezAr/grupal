import reflex as rx

from grupal.views.auth.login_form import login_form


@rx.page(
    route="/login",
    title="Login",
)
def login_page() -> rx.Component:
    return login_form()
