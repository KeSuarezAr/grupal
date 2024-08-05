from typing import List

import reflex as rx
import sqlalchemy

from sqlmodel import select

from grupal.models.user import UserModel


class UserState(rx.State):
    users: List[UserModel]

    def get_users(self, role: str = None):
        with rx.session() as session:
            query = select(UserModel).options(
                sqlalchemy.orm.selectinload(UserModel.person)
            )
            if role:
                query = query.where(UserModel.role == role)
            self.users = list(session.exec(query).all())

    def delete_user(self, user_id: int):
        with rx.session() as session:
            user = session.exec(UserModel.select().where(UserModel.id == user_id)).first()
            if user:
                session.delete(user)
                session.commit()
                self.users = [u for u in self.users if u.id != user_id]
            else:
                print(f"User with id {user_id} not found")
