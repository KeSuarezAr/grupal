from typing import Optional

import reflex as rx
import sqlalchemy
import sqlmodel

from grupal.models.admin import AdminModel
from grupal.models.parent import ParentModel
from grupal.models.profesor import ProfesorModel
from grupal.models.student import StudentModel
from grupal.models.user import UserModel


def select_all(role: Optional[str] = None) -> list[UserModel]:
    with rx.session() as session:
        consulta = sqlmodel.select(UserModel).options(
            sqlalchemy.orm.selectinload(UserModel.person),
        )
        if role:
            consulta = consulta.where(UserModel.role == role)
        user = session.exec(consulta)
        return list(user)


def insert_admin_user(user: dict):
    user = UserModel(username=user["username"], email=user["email"], password=user["password"], role="admin")
    with rx.session() as session:
        session.add(user)
        session.commit()
        session.refresh(user)

        admin = AdminModel(user_id=user.id)
        session.add(admin)
        session.commit()


def insert_profesor_user(user: dict):
    user = UserModel(username=user["username"], email=user["email"], password=user["password"], role="profesor")
    with rx.session() as session:
        session.add(user)
        session.commit()
        session.refresh(user)

        profesor = ProfesorModel(user_id=user.id)
        session.add(profesor)
        session.commit()


def insert_parent_user(user: dict):
    user = UserModel(username=user["username"], email=user["email"], password=user["password"], role="parent")
    with rx.session() as session:
        session.add(user)
        session.commit()
        session.refresh(user)

        parent = ParentModel(user_id=user.id)
        session.add(parent)
        session.commit()


def insert_student_user(user: dict):
    user = UserModel(username=user["username"], email=user["email"], password=user["password"], role="student")
    with rx.session() as session:
        session.add(user)
        session.commit()
        session.refresh(user)

        student = StudentModel(user_id=user.id)
        session.add(student)
        session.commit()


def delete_user(user_id: int):
    with rx.session() as session:
        session.delete(session.get(UserModel, user_id))
        session.commit()
