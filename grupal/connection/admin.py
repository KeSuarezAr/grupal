import reflex as rx

from grupal.models.admin import AdminModel
from grupal.models.user import UserModel


def insert_admin_user(user: dict):
    user = UserModel(username=user["username"], email=user["email"], password=user["password"], role="admin")
    print(user)
    with rx.session() as session:
        session.add(user)
        session.commit()
        session.refresh(user)

        admin = AdminModel(user_id=user.id)
        session.add(admin)
        session.commit()
