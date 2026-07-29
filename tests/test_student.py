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

    def test_classification_boundary_799(self):
        student = Student(
            "SV001",
            "Nguyen Van A",
            20,
            "CNTT",
            8.0,
            8.0,
            7.97
        )

        self.assertAlmostEqual(student.average_score(), 7.99, places=2)
        self.assertEqual(student.classification(), "Khá")
        
    def test_average_score_with_different_scores(self):
        student = Student(
                "SV002",
                "Tran Van B",
                21,
                "CNTT",
                9,
                5,
                7
            )

        self.assertAlmostEqual(student.average_score(), 7.0)
        self.assertEqual(student.classification(), "Khá")
            
            
if __name__ == "__main__":
    unittest.main()
