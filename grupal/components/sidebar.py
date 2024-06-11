import reflex as rx


def build_sidebar(items) -> rx.Component:
    return rx.container(
        rx.vstack(
            rx.vstack(
                rx.text("Proyecto", size="5"),
                rx.menu.root(
                    rx.menu.trigger(rx.button("Projects V", variant="soft")),
                    rx.menu.content(
                        *[
                            rx.menu.item(
                                rx.link(rx.text(title), route=f"/{title}"),
                                on_click=rx.redirect(f"/{title}"),
                            )
                            for title in items
                        ],
                    ),
                ),
            ),
            rx.vstack(
                rx.link(rx.text("Dashboard", size="5"), route="/"),
                rx.link(rx.text("Task Tracking", size="5"), route="/task-tracking"),
                rx.link(rx.text("Task History", size="5"), route="/task-history"),
                spacing="8",
            ),
            rx.button("Nueva Tarea", on_click=rx.redirect("/newtask"), size="4"),
            align="center",
            spacing="9",
        ),
        height="100vh",
        padding="20px",
        background_color="black",
        flex_grow=1,
        justify_content="center",
    )
