import reflex as rx
import sqlalchemy
import sqlmodel
from typing import Optional
from datetime import datetime

from sqlmodel import Field


class AssignmentModel(rx.Model, table=True):
    id: Optional[int] = sqlmodel.Field(default=None, primary_key=True)

    name: str
    category: str

    create_date: datetime = sqlmodel.Field(
        default=None,
        sa_column=sqlalchemy.Column(
            "create_date",
            sqlalchemy.DateTime(timezone=True),
            server_default=sqlalchemy.func.now(),
        ),
    )

    modify_date: datetime = sqlmodel.Field(
        default=None,
        sa_column=sqlalchemy.Column(
            "modify_date",
            sqlalchemy.DateTime(timezone=True),
            server_default=sqlalchemy.func.now(),
            onupdate=sqlalchemy.func.now(),
        ),
    )

    # trimester_id: Optional[int] = sqlmodel.Field(foreign_key="trimestermodel.id")
    # trimester: Optional["TrimesterModel"] = sqlmodel.Relationship(back_populates="assignments")

# from grupal.models.trimester import TrimesterModel
