from typing import Optional

import reflex as rx
import sqlmodel


class StudentModel(rx.Model, table=True):
    id: Optional[int] = sqlmodel.Field(default=None, primary_key=True)
    user_id: Optional[int] = sqlmodel.Field(foreign_key="usermodel.id")
    user: Optional["UserModel"] = sqlmodel.Relationship(back_populates="student")
    tuition: Optional["TuitionModel"] = sqlmodel.Relationship(back_populates="student")


from grupal.models.user import UserModel
from grupal.models.tuition import TuitionModel
