import reflex as rx
import sqlalchemy

from sqlmodel import select

from grupal.models.user import UserModel


class ProfileState(rx.State):
    user: UserModel = None

    def get_user_by_id(self):
        with (rx.session() as session):
            query = select(UserModel).options(
                sqlalchemy.orm.selectinload(UserModel.person)
            )
            query.where(UserModel.id == self.router.page.params.get("user_id"))
            self.user = session.exec(query).first()
