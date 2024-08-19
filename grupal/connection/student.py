import reflex as rx

from grupal.models.student import StudentModel


def insert_student_user(user: dict):
    user = StudentModel(
        username=user["username"],
        email=user["email"],
        password=user["password"],
        # role="student"
    )

    with rx.session() as session:
        session.add(user)
        session.commit()
        session.refresh(user)

        student = StudentModel(user_id=user.id)
        session.add(student)
        session.commit()
