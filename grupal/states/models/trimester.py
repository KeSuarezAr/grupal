from typing import List

import reflex as rx
import sqlalchemy.orm
from sqlmodel import select

from grupal.models.trimester import TrimesterModel


class TrimesterState(rx.State):
    trimesters: List[TrimesterModel]

    def get_trimesters(self):
        with rx.session() as session:
            query = select(TrimesterModel).options(
                sqlalchemy.orm.selectinload(TrimesterModel.assignments)
            )
            self.trimesters = list(session.exec(query).all())

    def delete_trimester(self, trimester_id: int):
        with rx.session() as session:
            trimester = session.exec(TrimesterModel.select().where(TrimesterModel.id == trimester_id)).first()
            if trimester:
                session.delete(trimester)
                session.commit()
                self.trimesters = [t for t in self.trimesters if t.id != trimester_id]
            else:
                print(f"Trimester with id {trimester_id} not found")
