import reflex as rx

from typing import Optional, List
from sqlmodel import Field, Relationship


class TrimesterModel(rx.Model, table=True): 
    id: Optional[int] = Field(primary_key=True)
    name: str
    description: str

    # assignments: List[Optional["AssignmentModel"]] = Relationship(back_populates="trimester")


# from grupal.models.assignment import AssignmentModel
