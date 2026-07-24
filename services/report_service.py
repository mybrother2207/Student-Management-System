import os
import csv

def export_csv(students):

    # Tự tạo thư mục reports nếu chưa có
    os.makedirs("reports", exist_ok=True)

    with open(
        "reports/students.csv",
        "w",
        newline="",
        encoding="utf-8-sig"
    ) as file:

        writer = csv.writer(file)

        writer.writerow([
            "Mã",
            "Tên",
            "Tuổi",
            "Ngành",
            "Toán",
            "Văn",
            "Anh",
            "GPA",
            "Xếp loại"
        ])

        for student in students:
            writer.writerow([
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

    print("Xuất CSV thành công.")