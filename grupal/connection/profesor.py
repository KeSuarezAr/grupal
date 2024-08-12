import reflex as rx

from grupal.models.teacher import TeacherModel
from grupal.models.user import UserModel


def insert_profesor_user(user: dict):
    user = UserModel(username=user["username"], email=user["email"], password=user["password"], role="profesor")
    with rx.session() as session:
        session.add(user)
        session.commit()
        session.refresh(user)

        profesor = TeacherModel(user_id=user.id)
        session.add(profesor)
        session.commit()
