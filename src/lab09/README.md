# python_labs

## Лабораторная работа 9

### Задание A
 
 #### group

 <img width="1526" height="2610" alt="Group" src="https://github.com/user-attachments/assets/d596714e-62ba-45bc-be40-fc8e01a45a2c" />


```
import csv
from pathlib import Path
from src.lab08.models import Student
class Group:
    def __init__(self, storage_path: str):
        self.path = Path(storage_path)
        if not self.path.exists():
            self.path.parent.mkdir(parents=True, exist_ok=True)
            with open(self.path, "w", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow(["fio", "birthdate", "group", "gpa"])

    def _read_all(self) -> list[Student]:
        students = []
        with open(self.path, encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                students.append(
                    Student(
                        fio=row["fio"],
                        birthdate=row["birthdate"],
                        group=row["group"],
                        gpa=float(row["gpa"]),
                    )
                )
        return students

    def list(self) -> list[Student]:
        return self._read_all()

    def add(self, student: Student):
        with open(self.path, "a", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(
                [student.fio, student.birthdate, student.group, student.gpa]
            )

    def find(self, substr: str):
        return [s for s in self._read_all() if substr.lower() in s.fio.lower()]

    def remove(self, fio: str):
        students = [s for s in self._read_all() if s.fio != fio]
        with open(self.path, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["fio", "birthdate", "group", "gpa"])
            for s in students:
                writer.writerow([s.fio, s.birthdate, s.group, s.gpa])

    def update(self, fio: str, **fields):
        students = self._read_all()
        for s in students:
            if s.fio == fio:
                for k, v in fields.items():
                    setattr(s, k, v)

        with open(self.path, "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["fio", "birthdate", "group", "gpa"])
            for s in students:
                writer.writerow([s.fio, s.birthdate, s.group, s.gpa])

```


#### Students

<img width="772" height="444" alt="students" src="https://github.com/user-attachments/assets/42136b24-7a2c-47ae-a762-4215a29cf6f7" />


```
fio,birthdate,group,gpa
Ana Lopez,2001-03-15,SE-02,5.0
Juan Perez,2002-05-10,SE-03,4.9

```

  #### Result 

  
  <img width="1201" height="118" alt="list()" src="https://github.com/user-attachments/assets/0d195f09-6d9e-4de5-978a-a54900f1a948" />


<img width="707" height="67" alt="find()" src="https://github.com/user-attachments/assets/fcf57416-e0b9-4439-8063-46140d438904" />


<img width="1192" height="290" alt="add" src="https://github.com/user-attachments/assets/f8f4b054-20bd-4cb0-8118-404e886db6f7" />

<img width="1173" height="157" alt="remove" src="https://github.com/user-attachments/assets/5b3f541e-0306-429b-9cd1-dd1a034923da" />

<img width="845" height="183" alt="update" src="https://github.com/user-attachments/assets/d0f38924-83d3-4f65-8260-574c1705f9b5" />

  
