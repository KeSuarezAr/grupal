import reflex as rx

from grupal.views.student_profile import student_profile


@rx.page(
    route="/student/[user_id]",
    title="Estudiante",
)
def student_page() -> rx.Component:
    return rx.flex(
        rx.color_mode.button(position="top-right"),
        rx.heading("Usuarios", size="5"),
        student_profile(),
        direction="column",
        gap="1rem",
        align="center",
        justify="center",

    )
