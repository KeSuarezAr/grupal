from typing import List

import reflex as rx
from sqlmodel import select

from grupal.models.assignment import AssignmentModel
from grupal.models.user import UserModel


class AssignmentState(rx.State):
    assignments: List[AssignmentModel]

    def get_assignments(self):
        with rx.session() as session:
            query = select(AssignmentModel)
            self.assignments = list(session.exec(query).all())

    def delete_assignment(self, assignment_id: int):
        with rx.session() as session:
            assignment = session.exec(UserModel.select().where(UserModel.id == assignment_id)).first()
            if assignment:
                session.delete(assignment)
                session.commit()
                self.assignments = [a for a in self.assignments if a.id != assignment_id]
            else:
                print(f"Assignment with id {assignment_id} not found")
