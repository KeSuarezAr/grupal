import reflex as rx

from grupal.states.models.assignment import AssignmentState
from grupal.views.lists.assignments_list import asignaciones_table


@rx.page(
    on_load=AssignmentState.get_assignments,
    route="/assignments",
    title="Asignaciones",
)
def asignments_page() -> rx.Component:
    return rx.flex(
        rx.color_mode.button(position="top-right"),
        rx.heading("Asignaciones", size="5"),
        rx.flex(
            direction="row",
            gap="1rem",
        ),
        asignaciones_table(AssignmentState.assignments),
        direction="column",
        gap="1rem",
    )
