import reflex as rx
from bcrypt import checkpw, gensalt, hashpw
from sqlmodel import select

from grupal.models.user import UserModel


def login_user(login_form: dict) -> tuple[UserModel, str] | None:
    email = login_form["email"]
    password = login_form["password"].encode("utf-8")

    with rx.session() as session:
        user = session.exec(
            select(UserModel).where(UserModel.email == email)
        ).first()

        if user and checkpw(password, user.password.encode("utf-8")):
            return user

    return None


def register_user(register_form: dict):
    username = register_form["username"]
    email = register_form["email"]
    password = register_form["password"].encode("utf-8")

    with rx.session() as session:
        user = UserModel(
            username=username,
            email=email,
            password=hashpw(password, gensalt()).decode("utf-8"),
            role="estudiante",
        )
        session.add(user)
        session.commit()

    return True
