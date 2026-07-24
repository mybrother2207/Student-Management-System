import json
from models.student import Student

FILE_NAME = "students.json"


def save_students(students):
    data = []

    for student in students:
        data.append(student.to_dict())

    with open(FILE_NAME, "w", encoding="utf-8") as file:
        json.dump(
            data,
            file,
            ensure_ascii=False,
            indent=4
        )

    print("\nĐã lưu dữ liệu thành công.")


def load_students():
    try:
        with open(FILE_NAME, "r", encoding="utf-8") as file:
            data = json.load(file)

        students = []

        for item in data:
            students.append(Student.from_dict(item))

        return students

    except FileNotFoundError:
        return []

    except json.JSONDecodeError:
        return []