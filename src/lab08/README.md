# python_labs

## Лабораторная работа 8

### Задание A
 
 #### Models

<img width="1388" height="1964" alt="models" src="https://github.com/user-attachments/assets/42421532-a8be-4f8f-a60a-8100925b7fb9" />
 

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

<img width="1356" height="900" alt="demo" src="https://github.com/user-attachments/assets/47bfd8d4-276b-46e3-85ae-0ccde1a16475" />

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

<img width="743" height="217" alt="Demo_result" src="https://github.com/user-attachments/assets/d040bbd0-a697-4bf5-8703-0ab4515e6130" />
        
#### Result 


<img width="825" height="283" alt="age_dict" src="https://github.com/user-attachments/assets/506f9c8f-95a2-4edf-8d0b-b68d73a3d3f0" />


<img width="731" height="257" alt="from_dict" src="https://github.com/user-attachments/assets/cb555a10-15fe-48ee-9dc8-18c819752a44" />


### Задание B

#### Serialize

<img width="1172" height="900" alt="serialize" src="https://github.com/user-attachments/assets/6d0c703b-34fb-4520-a789-eb50c54a2fd0" />

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

<img width="772" height="862" alt="studento_input" src="https://github.com/user-attachments/assets/3ff4b950-ec68-45b8-bee0-b413f3019655" />


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
<img width="1719" height="1017" alt="Result-student" src="https://github.com/user-attachments/assets/002bc799-d258-4e83-a057-fec05abadd20" />
