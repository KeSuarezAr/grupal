from typing import Optional

from reflex import Model
from sqlmodel import Field, Relationship


class ProfesorModel(Model, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    user_id: Optional[int] = Field(foreign_key="usermodel.id")
    user: Optional["UserModel"] = Relationship(back_populates="profesor")


from grupal.models.user import UserModel
