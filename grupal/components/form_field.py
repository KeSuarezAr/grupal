from typing import Optional

import reflex as rx


def form_field(label: str, placeholder: str, input_type: str, field_name: str, field_value: Optional[str] = None):
    return rx.hstack(
        rx.icon("layout-dashboard", size=16, stroke_width=1.5),
        rx.input(
            placeholder=placeholder,
            type=input_type,
            name=field_name,
            value=field_value,
        ),
        rx.text(label),
    )
