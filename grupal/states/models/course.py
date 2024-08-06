from typing import List

import reflex as rx
import sqlalchemy

from sqlmodel import select

from grupal.models.course import CourseModel


class CourseState(rx.State):
    courses: List[CourseModel]

    def get_courses(self):
        with rx.session() as session:
            query = select(CourseModel)
            self.courses = list(session.exec(query).all())

    def delete_course(self, course_id: int):
        with rx.session() as session:
            course = session.exec(CourseModel.select().where(CourseModel.id == course_id)).first()
            if course:
                session.delete(course)
                session.commit()
                self.courses = [c for c in self.courses if c.id != course_id]
            else:
                print(f"Course with id {course_id} not found")
