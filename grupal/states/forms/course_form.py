import reflex as rx

from grupal.models.course import CourseModel


class CourseFormState(rx.State):
    new_course: dict = {
        "name": "",
        "paralelo": "",
    }

    def set_name(self, name):
        self.new_course["name"] = name

    def set_paralelo(self, paralelo):
        self.new_course["paralelo"] = paralelo

    def add_course(self):
        with rx.session() as session:
            course = CourseModel(
                name=self.new_course["name"],
                paralelo=self.new_course["paralelo"],
            )

            session.add(course)
            session.commit()
            session.refresh(course)
