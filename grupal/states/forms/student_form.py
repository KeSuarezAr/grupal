import reflex as rx

from grupal.connection.student import insert_student_user
from grupal.models.person import PersonModel
from grupal.models.user import UserModel


class StudentFormState(rx.State):
    new_user: dict = {
        "username": "",
        "email": "",
        "password": "",
        "first_name": "",
        "last_name": "",
        "cedula": "",
        "address": "",
    }

    def set_username(self, username):
        self.new_user["username"] = username

    def set_email(self, email):
        self.new_user["email"] = email

    def set_password(self, password):
        self.new_user["password"] = password

    def set_first_name(self, first_name):
        self.new_user["first_name"] = first_name

    def set_last_name(self, last_name):
        self.new_user["last_name"] = last_name

    def set_cedula(self, cedula):
        self.new_user["cedula"] = cedula

    def set_address(self, address):
        self.new_user["address"] = address

    def add_student(self):
        with rx.session() as session:
            user = UserModel(
                username=self.new_user["username"],
                email=self.new_user["email"],
                password=self.new_user["password"],
                role="student",
            )

            session.add(user)
            session.commit()
            session.refresh(user)

            person = PersonModel(
                first_name=self.new_user["first_name"],
                last_name=self.new_user["last_name"],
                cedula=self.new_user["cedula"],
                address=self.new_user["address"],
                user_id=user.id,
            )

            session.add(person)
            session.commit()
            session.refresh(person)

            student = insert_student_user(self.new_user)
            session.commit()
            session.refresh(student)