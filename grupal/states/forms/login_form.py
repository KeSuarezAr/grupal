import reflex as rx

from grupal.connection.auth import login_user


class LoginFormState(rx.State):
    user: dict = {
        "email": "",
        "password": "",
    }

    def set_email(self, email):
        self.user["email"] = email

    def set_password(self, password):
        self.user["password"] = password

    def login(self):
        user = login_user(self.user)
        if user is None:
            return rx.redirect("/login")
