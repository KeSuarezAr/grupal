from typing import Optional

from reflex import Model
from sqlmodel import Field, Relationship


class CourseModel(Model, table=True):
    id: Optional[int] = Field(primary_key=True)
    name: str
    paralelo: str
