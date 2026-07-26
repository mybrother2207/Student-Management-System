
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

    def display(self):
        print("-" * 40)
        print("Mã:", self.student_id)
        print("Tên:", self.name)
        print("Tuổi:", self.age)
        print("Ngành:", self.major)
        print("Toán:", self.math)
        print("Văn:", self.literature)
        print("Anh:", self.english)
        print("GPA:", self.average_score())
        print("Xếp loại:", self.classification())
        print("-" * 40)

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
            data.get("math",0),
            data.get("literature",0),
            data.get("english",0)
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


