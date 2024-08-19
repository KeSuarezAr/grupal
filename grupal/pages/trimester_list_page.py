import reflex as rx

from grupal.states.models.trimester import TrimesterState
from grupal.components.forms.trimester_form import trimester_dialogue
from grupal.components.lists.trimesters_list import trimesters_table


@rx.page(
    on_load=TrimesterState.get_trimesters,
    route="/trimesters",
    title="Trimestres",
)
def trimesters_page() -> rx.Component:
    return rx.flex(
        rx.color_mode.button(position="top-right"),
        rx.heading("Trimestres", size="5"),
        trimester_dialogue(),
        trimesters_table(TrimesterState.trimesters),
        direction="column",
        gap="1rem",
    )
