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
