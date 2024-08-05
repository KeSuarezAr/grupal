import sqlmodel
import reflex as rx

from typing import Optional


class TeacherSubjectParallelAssignment(rx.Model, table=True):
    id: Optional[int] = sqlmodel.Field(default=None, primary_key=True)
    teacher_id: int
    subject_id: int
    parallel: str
    assignment_id: Optional[int] = sqlmodel.Field(foreign_key="assignment.id")


from grupal.models.assignment import AssignmentModel
