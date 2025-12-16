# python_labs

## Лабораторная работа 8

### Задание A

<img width="1880" height="3446" alt="Tarea_A" src="https://github.com/user-attachments/assets/342e99f1-473e-4621-a251-7196d1b08b29" />
 
 #### Models

```
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

```

#### Demo

```
from src.lab08.models import Student
from src.lab08.serialize import students_to_json, students_from_json

students = [
    Student("Juan Perez", "2002-05-10", "SE-01", 4.3),
    Student("Maria Lopez", "2001-08-21", "SE-02", 4.8),
]

students_to_json(students, "data/lab08/students_output.json")

loaded = students_from_json("data/lab08/students_output.json")

for s in loaded:
    print(s)
    print("Edad:", s.age())

```

        
<img width="1046" height="131" alt="Tarea_A result" src="https://github.com/user-attachments/assets/068bfbf1-fe08-479d-8d5c-33be4041f138" />

### Задание B

#### Serialize

<img width="1664" height="2762" alt="Tarea_B" src="https://github.com/user-attachments/assets/57edc4da-ca2e-423e-8196-ad0e85ae8fa3" />

 ```
import json
from src.lab08.models import Student


def students_to_json(students, path):
    data = [s.to_dict() for s in students]
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def students_from_json(path):
    with open(path, "r", encoding="utf-8") as f:
        data = json.load(f)

    return [Student.from_dict(item) for item in data]

```
#### JSON 

```
[
  {
    "fio": "Ana Lopez",
    "birthdate": "2001-03-15",
    "group": "SE-02",
    "gpa": 4.8
  },
  {
    "fio": "Carlos Ruiz",
    "birthdate": "2000-11-02",
    "group": "SE-01",
    "gpa": 3.9
  }
]
```
