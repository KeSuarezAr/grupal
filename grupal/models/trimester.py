from typing import Optional

import reflex as rx
from sqlmodel import Field


class TrimesterModel(rx.Model, table=True):
    id: Optional[int] = Field(primary_key=True)
    name: str
    description: str

    # assignments: List[Optional["AssignmentModel"]] = Relationship(back_populates="trimester")

# from grupal.models.assignment import AssignmentModel
