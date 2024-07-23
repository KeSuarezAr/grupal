from datetime import datetime
from typing import Optional

import reflex as rx
from sqlmodel import Field, Relationship


class TuitionModel(rx.Model, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    date: datetime
    cod: str
    precio: float

    student_id: Optional[int] = Field(foreign_key="studentmodel.id")
    student: Optional["StudentModel"] = Relationship(back_populates="tuition")


from grupal.models.student import StudentModel
