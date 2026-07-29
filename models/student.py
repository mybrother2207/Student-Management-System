class Student:
    def __init__(
        self,
        student_id,
        name,
        age,
        major,
        math,
        literature,
        english
    ):
        self.student_id = student_id
        self.name = name
        self.age = age
        self.major = major
        self.math = math
        self.literature = literature
        self.english = english

    def __str__(self):
        return (
            "-" * 40 + "\n"
            f"Mã: {self.student_id}\n"
            f"Tên: {self.name}\n"
            f"Tuổi: {self.age}\n"
            f"Ngành: {self.major}\n"
            f"Toán: {self.math}\n"
            f"Văn: {self.literature}\n"
            f"Anh: {self.english}\n"
            f"GPA: {self.average_score():.2f}\n"
            f"Xếp loại: {self.classification()}\n"
            + "-" * 40
        )

    def to_dict(self):
        return {
            "student_id": self.student_id,
            "name": self.name,
            "age": self.age,
            "major": self.major,
            "math": self.math,
            "literature": self.literature,
            "english": self.english
        }

    @staticmethod
    def from_dict(data):
        return Student(
            data["student_id"],
            data["name"],
            data["age"],
            data["major"],
            data.get("math", 0),
            data.get("literature", 0),
            data.get("english", 0)
        )

    def average_score(self):
        return round(
            (self.math + self.literature + self.english) / 3,
            2
        )

    def classification(self):
        avg = self.average_score()

        if avg >= 8:
            return "Giỏi"
        elif avg >= 6.5:
            return "Khá"
        elif avg >= 5:
            return "Trung bình"

        return "Yếu"
