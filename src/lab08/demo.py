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

