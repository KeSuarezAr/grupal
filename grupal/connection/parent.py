import reflex as rx

from grupal.models.parent import ParentModel
from grupal.models.user import UserModel


def insert_parent_user(user: dict):
    user = UserModel(username=user["username"], email=user["email"], password=user["password"], role="parent")
    with rx.session() as session:
        session.add(user)
        session.commit()
        session.refresh(user)

        parent = ParentModel(user_id=user.id)
        session.add(parent)
        session.commit()
