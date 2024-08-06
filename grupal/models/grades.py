import reflex as rx
from typing import Optional
import sqlmodel


class FinalGrades(rx.Model, table=True):
    id: Optional[int] = sqlmodel.Field(default=None, primary_key=True)
    trimester1: float
    trimester2: float
    trimester3: float


class FinalGradesTrimester(rx.Model, table=True):
    id: Optional[int] = sqlmodel.Field(default=None, primary_key=True)
    individual_average: float
    group_average: float
    project_average: float
    exam_average: float
