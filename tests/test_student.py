import unittest
from models.student import Student


class TestStudent(unittest.TestCase):

    def test_average_score(self):
        student = Student(
            "SV001",
            "An",
            20,
            "CNTT",
            8,
            8,
            8
        )

        self.assertEqual(student.average_score(), 8.0)

    def test_classification_gioi(self):
        student = Student(
            "SV001",
            "An",
            20,
            "CNTT",
            8,
            8,
            8
        )

        self.assertEqual(student.classification(), "Giỏi")

    def test_classification_kha(self):
        student = Student(
            "SV001",
            "An",
            20,
            "CNTT",
            6.5,
            6.5,
            6.5
        )

        self.assertEqual(student.classification(), "Khá")

    def test_classification_trung_binh(self):
        student = Student(
            "SV001",
            "An",
            20,
            "CNTT",
            5,
            5,
            5
        )

        self.assertEqual(student.classification(), "Trung bình")

    def test_classification_yeu(self):
        student = Student(
            "SV001",
            "An",
            20,
            "CNTT",
            4,
            4,
            4
        )

        self.assertEqual(student.classification(), "Yếu")


if __name__ == "__main__":
    unittest.main()
