import reflex as rx

from grupal.models.admin import AdminModel
from grupal.models.person import PersonModel
from grupal.models.trimester import TrimesterModel
from grupal.models.user import UserModel


class TrimestreFormState(rx.State):
    new_trimester: dict = {
        "name": "",
        "description": "",
        "assignments": [],
    }

    def set_name(self, username):
        self.new_trimester["username"] = username

    def set_description(self, email):
        self.new_trimester["email"] = email

    def add_trimester(self):
        with rx.session() as session:
            trimester = TrimesterModel(
                name=self.new_trimester["username"],
                description=self.new_trimester["email"],
            )

            session.add(trimester)
            session.commit()
            session.refresh(trimester)
