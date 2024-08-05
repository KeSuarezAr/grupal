from typing import Optional

import sqlalchemy
import sqlmodel
from reflex import Model
from sqlmodel import Field, Relationship


class UserModel(Model, table=True):
    id: Optional[int] = Field(primary_key=True)
    username: str
    email: str
    password: str
    role: str

    person: Optional["PersonModel"] = Relationship(back_populates="user")

    admin: Optional["AdminModel"] = Relationship(back_populates="user")
    profesor: Optional["TeacherModel"] = Relationship(back_populates="user")
    parent: Optional["ParentModel"] = Relationship(back_populates="user")
    student: Optional["StudentModel"] = Relationship(back_populates="user")


from grupal.models.person import PersonModel
from grupal.models.admin import AdminModel
from grupal.models.parent import ParentModel
from grupal.models.student import StudentModel
from grupal.models.teacher import TeacherModel
