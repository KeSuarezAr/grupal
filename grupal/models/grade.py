import sqlmodel
import reflex as rx
from typing import Optional


class GradeModel(rx.Model, table=True):
    id: Optional[int] = sqlmodel.Field(default=None, primary_key=True)
    assignment_id: Optional[int] = sqlmodel.Field(foreign_key="assignmentmodel.id")
    grade: float
    grade_type: str


from grupal.models.assignment import AssignmentModel
