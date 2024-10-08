from datetime import datetime
from typing import Optional

import reflex as rx
import sqlmodel


class ContributionModel(rx.Model, table=True):
    id: Optional[int] = sqlmodel.Field(default=None, primary_key=True)
    assignment_id: Optional[int] = sqlmodel.Field(foreign_key="assignmentmodel.id")
    fecha_creacion: datetime = sqlmodel.Field(default_factory=datetime.utcnow)
    fecha_modificacion: datetime = sqlmodel.Field(default_factory=datetime.utcnow)
    tipo: str

# from grupal.models.assignment import AssignmentModel
