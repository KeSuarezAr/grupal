import sqlmodel
import reflex as rx

from typing import Optional, List


class QuantitativeGrade(rx.Model, table=True):
    id: Optional[int] = sqlmodel.Field(default=None, primary_key=True)
    value: float


class QualitativeGradeItem(rx.Model, table=True):
    id: Optional[int] = sqlmodel.Field(default=None, primary_key=True)
    minimum_range: float
    maximum_range: float
    name: str


class QualitativeGrade(rx.Model, table=True):
    id: Optional[int] = sqlmodel.Field(default=None, primary_key=True)
    category: str
    items: List[QualitativeGradeItem] = sqlmodel.Relationship()