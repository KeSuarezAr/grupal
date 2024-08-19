import reflex as rx

from grupal.components.navbar import navbar_docente
from grupal.components.table import docente_table


@rx.page("/docente", title="Docente")
def docente_page() -> rx.Component:
    return rx.vstack(
        navbar_docente(),
        rx.box(
            docente_table(),
            width="100%",
        ),
        width="100%",
        spacing="6",
        padding_x=["1.5em", "1.5em", "3em"],
    )