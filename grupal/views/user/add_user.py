import reflex as rx


def trigger_body(title: str) -> rx.Component:
    return rx.dialog.trigger(
        rx.button(f"Añadir {title} ", width="150px"),
    )


def content_body(title: str, set_username_callback: callable, set_email_callback: callable,
                 set_password_callback: callable,
                 add_user_callback: callable) -> rx.Component:
    return rx.dialog.content(
        rx.flex(
            rx.dialog.title(f"Añadir Usuario {title}"),
            product_form(set_username_callback, set_email_callback, set_password_callback, add_user_callback),
            justify="center",
            align="center",
            direction="column",
        ),
        style={"width": "400px", "padding": "10px"},
    )


def admin_dialogue(
        set_username_callback: callable,
        set_email_callback: callable,
        set_password_callback: callable,
        add_user_callback: callable,
) -> rx.Component:
    return rx.dialog.root(
        trigger_body("Admin"),
        content_body("Admin", set_username_callback, set_email_callback, set_password_callback, add_user_callback),
    )

def profesor_dialogue(
        set_username_callback: callable,
        set_email_callback: callable,
        set_password_callback: callable,
        add_user_callback: callable,
) -> rx.Component:
    return rx.dialog.root(
        trigger_body("Profesor"),
        content_body("Profesor", set_username_callback, set_email_callback, set_password_callback, add_user_callback),
    )


def student_dialogue(
        set_username_callback: callable,
        set_email_callback: callable,
        set_password_callback: callable,
        add_user_callback: callable,
) -> rx.Component:
    return rx.dialog.root(
        trigger_body("Estudiante"),
        content_body("Estudiante", set_username_callback, set_email_callback, set_password_callback, add_user_callback),
    )

def parent_dialogue(
        set_username_callback: callable,
        set_email_callback: callable,
        set_password_callback: callable,
        add_user_callback: callable,
) -> rx.Component:
    return rx.dialog.root(
        trigger_body("Padre"),
        content_body("Padre", set_username_callback, set_email_callback, set_password_callback, add_user_callback),
    )


def product_form(
        set_username_callback: callable,
        set_email_callback: callable,
        set_password_callback: callable,
        add_product_callback: callable,
) -> rx.Component:
    return rx.form(
        rx.input(
            placeholder="UserName",
            name="username",
            type="text",
            input_mode="text",
            on_change=set_username_callback,
        ),
        rx.input(
            placeholder="Email",
            name="email",
            type="text",
            input_mode="text",
            on_change=set_email_callback,
        ),
        rx.input(
            placeholder="Password",
            name="password",
            type="password",
            input_mode="text",
            on_change=set_password_callback,
        ),
        rx.button(
            "Guardar",
            type="submit",
            on_click=add_product_callback,
        ),
        rx.dialog.close(
            rx.button("Cancelar", variant="soft", color_scheme="red"),
        ),
        reset_on_submit=True,
        justify="center",
        align="center",
    )
