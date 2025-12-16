from dataclasses import dataclass
from datetime import date, datetime
@dataclass
class Student:
    fio: str
    birthdate: str  
    group: str
    gpa: float

    def __post_init__(self):
        try:
            datetime.strptime(self.birthdate, "%Y-%m-%d")
        except ValueError:
            raise ValueError("birthdate must be in YYYY-MM-DD format")
        if not (0 <= self.gpa <= 5):
            raise ValueError("gpa must be between 0 and 5")

    def age(self) -> int:
        bdate = datetime.strptime(self.birthdate, "%Y-%m-%d").date()
        today = date.today()
        return today.year - bdate.year - (
            (today.month, today.day) < (bdate.month, bdate.day)
        )

    def to_dict(self) -> dict:
        return {
            "fio": self.fio,
            "birthdate": self.birthdate,
            "group": self.group,
            "gpa": self.gpa,
        }

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            fio=data["fio"],
            birthdate=data["birthdate"],
            group=data["group"],
            gpa=data["gpa"],
        )

    def __str__(self):
        return f"{self.fio} ({self.group}) — GPA: {self.gpa}"
