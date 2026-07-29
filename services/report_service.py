from openpyxl import Workbook
import os


def export_excel(students, file_path="reports/students.xlsx"):

    directory = os.path.dirname(file_path)
    if directory:
        os.makedirs(directory, exist_ok=True)

    wb = Workbook()
    ws = wb.active
    ws.title = "Students"

    ws.append([
        "Mã SV",
        "Họ tên",
        "Tuổi",
        "Ngành",
        "Toán",
        "Văn",
        "Tiếng Anh",
        "GPA",
        "Xếp loại"
    ])

    for student in students:
        ws.append([
            student.student_id,
            student.name,
            student.age,
            student.major,
            student.math,
            student.literature,
            student.english,
            student.average_score(),
            student.classification()
        ])

    wb.save(file_path)

    print(f"\nXuất Excel thành công:\n{file_path}")
