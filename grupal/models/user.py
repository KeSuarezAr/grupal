from typing import Optional

from reflex import Model
from sqlmodel import Field, Relationship


class UserModel(Model, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    username: str
    email: str
    password: str
    role: str

    person: Optional["PersonModel"] = Relationship(back_populates="user")

    admin: Optional["AdminModel"] = Relationship(back_populates="user")
    profesor: Optional["ProfesorModel"] = Relationship(back_populates="user")
    parent: Optional["ParentModel"] = Relationship(back_populates="user")
    student: Optional["StudentModel"] = Relationship(back_populates="user")


from grupal.models.admin import AdminModel
from grupal.models.profesor import ProfesorModel
from grupal.models.parent import ParentModel
from grupal.models.person import PersonModel
from grupal.models.student import StudentModel
