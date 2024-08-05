import reflex as rx

from grupal.views.forms.login_form import login_form


@rx.page(
    route="/login",
    title="Login",
)
def login_page() -> rx.Component:
    return login_form()
