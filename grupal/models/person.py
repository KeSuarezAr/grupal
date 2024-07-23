from typing import Optional

import reflex as rx
import sqlmodel


class PersonModel(rx.Model, table=True):
    id: Optional[int] = sqlmodel.Field(default=None, primary_key=True)

    first_name: str
    last_name: str
    cedula: str
    address: str

    user_id: Optional[int] = sqlmodel.Field(foreign_key="usermodel.id")
    user: Optional["UserModel"] = sqlmodel.Relationship(back_populates="person")


from grupal.models.user import UserModel
