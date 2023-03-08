from dataclasses import dataclass
from typing import Optional


@dataclass
class Student:
    name: str
    lastname: str
    clas: str
    attendance: str
    grade: int
    id: Optional[int] = None