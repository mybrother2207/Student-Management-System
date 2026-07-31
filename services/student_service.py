from models.student import Student
from utils.validator import (
    is_duplicate_id,
    is_valid_age,
    is_valid_name,
    is_valid_major,
    input_score
)

from services.file_service import save_students, load_students
from services.logger_config import logger
# Danh sách lưu sinh viên
students = []


# ==========================
# Thêm sinh viên
# ==========================
def add_student():

    print("\n===== THÊM SINH VIÊN =====")

    # Nhập mã sinh viên
    while True:
        student_id = input("Mã sinh viên: ").strip()

        if student_id == "":
            print(">> Mã sinh viên không được để trống.")
            continue

        if is_duplicate_id(students, student_id):
            print(">> Mã sinh viên đã tồn tại.")
            continue

        break

    # Nhập họ tên
    while True:
        name = input("Họ tên: ").strip()

        if name == "":
            print(">> Họ tên không được để trống.")
            continue

        if not is_valid_name(name):
            print(">> Họ tên không hợp lệ.")
            continue

        break

    # Nhập tuổi
    while True:
        try:
            age = int(input("Tuổi: "))

            if not is_valid_age(age):
                print(">> Tuổi phải lớn hơn 0.")
                continue

            break

        except ValueError:
            print(">> Tuổi phải là số nguyên.")

    # Nhập ngành học
    while True:
        major = input("Ngành học: ").strip()

        if major == "":
            print(">> Ngành học không được để trống.")
            continue

        if not is_valid_major(major):
            print(">> Ngành học không hợp lệ.")
            continue

        break

    # Nhập điểm
    print("\n===== NHẬP ĐIỂM =====")

    math = input_score("Toán")
    literature = input_score("Văn")
    english = input_score("Anh")

    # Tạo sinh viên
    student = Student(
        student_id,
        name,
        age,
        major,
        math,
        literature,
        english
    )

    # Thêm vào danh sách
    students.append(student)

    # Lưu dữ liệu
    save_students(students)

    # Ghi log
    logger.info(
        f"Thêm sinh viên: {student.student_id} - "
        f"{student.name}"
    )

    print("\n===================================")
    print("✓ THÊM SINH VIÊN THÀNH CÔNG!")
    print("===================================")

    print("\nThông tin sinh viên vừa thêm:")
    print(student)
# ==========================
# Hiển thị danh sách
# ==========================


def show_students():
    print("\n===== DANH SÁCH SINH VIÊN =====")

    if len(students) == 0:
        print("Danh sách rỗng.")
        return

    for index, student in enumerate(students, start=1):

        print(f"\n===== Sinh viên {index} =====")

        print(student)


# ==========================
# Tìm kiếm sinh viên
# ==========================
def find_student():
    print("\n===== TÌM KIẾM SINH VIÊN =====")

    student_id = input("Nhập mã sinh viên: ").strip()

    for student in students:
        if student.student_id == student_id:
            print("\nĐã tìm thấy sinh viên:")
            print(student)
            return

    print("Không tìm thấy sinh viên.")


# ==========================
# Cập nhật sinh viên
# ==========================
def update_student():

    print("\n===== CẬP NHẬT SINH VIÊN =====")

    student_id = input("Nhập mã sinh viên: ").strip()

    for student in students:

        if student.student_id == student_id:

            # Cập nhật tên
            while True:
                name = input(f"Tên [{student.name}]: ").strip()

                if name == "":
                    name = student.name
                    break

                if is_valid_name(name):
                    break

                print("Tên không hợp lệ.")

            # Cập nhật tuổi
            while True:

                age = input(f"Tuổi [{student.age}]: ").strip()

                if age == "":
                    age = student.age
                    break

                try:
                    age = int(age)

                    if is_valid_age(age):
                        break

                    print("Tuổi phải lớn hơn 0.")

                except ValueError:
                    print("Tuổi phải là số.")

            # Cập nhật ngành
            while True:

                major = input(f"Ngành [{student.major}]: ").strip()

                if major == "":
                    major = student.major
                    break

                if is_valid_major(major):
                    break

                print("Ngành không hợp lệ.")

            # Lưu thông tin mới
            student.name = name
            student.age = age
            student.major = major

            student.math = input_score("Toán", student.math)
            student.literature = input_score("Văn", student.literature)
            student.english = input_score("Anh", student.english)
            save_students(students)
            logger.info(
                f"Cập nhật sinh viên: {student.student_id}"
            )

            print("\n>> Cập nhật thành công.")
            return

    print("Không tìm thấy sinh viên.")


# ==========================
# Xóa sinh viên
# ==========================
def delete_student():
    print("\n===== XÓA SINH VIÊN =====")

    student_id = input("Nhập mã sinh viên cần xóa: ").strip()

    for student in students:

        if student.student_id == student_id:

            print("\nThông tin sinh viên:")
            print(student)

            while True:
                confirm = (
                    input("Bạn có chắc muốn xóa? (Y/N): ")
                    .strip()
                    .upper()
                )

                if confirm == "Y":
                    students.remove(student)
                    save_students(students)
                    logger.info(f"Xóa sinh viên: {student.student_id}")
                    print("\n>> Xóa sinh viên thành công!")
                    return

                elif confirm == "N":
                    print("\n>> Đã hủy xóa.")
                    return

                else:
                    print(">> Vui lòng nhập Y hoặc N.")

    print("\n>> Không tìm thấy sinh viên.")


# ==========================
# Tìm theo tên
# ==========================
def search_by_name():

    keyword = input("Nhập tên cần tìm: ").strip().lower()

    found = False

    for student in students:

        if keyword in student.name.lower():
            print(student)
            found = True

    if not found:
        print(">> Không tìm thấy sinh viên.")


# ==========================
# Tìm theo ngành
# ==========================
def search_by_major():

    keyword = input("Nhập ngành: ").strip().lower()

    found = False

    for student in students:

        if keyword in student.major.lower():
            print(student)
            found = True

    if not found:
        print(">> Không tìm thấy sinh viên.")


# ==========================
# Thống kê
# ==========================
def statistic():

    print("\n===== THỐNG KÊ =====")

    counts = {
        "Giỏi": 0,
        "Khá": 0,
        "Trung bình": 0,
        "Yếu": 0
    }

    for student in students:
        counts[student.classification()] += 1

    print(f"Tổng số sinh viên: {len(students)}\n")

    for rank, total in counts.items():
        print(f"{rank:<12}: {total}")


# ==========================
# Sắp xếp GPA giảm dần
# ==========================
def sort_gpa():

    print("\n===== DANH SÁCH THEO GPA =====")

    if not students:
        print("Danh sách rỗng.")
        return

    sorted_students = sorted(
        students,
        key=lambda x: x.average_score(),
        reverse=True
    )

    for index, student in enumerate(sorted_students, start=1):
        print(f"\n----- {index} -----")
        print(student)


# ==========================
# Khởi tạo danh sách sinh viên
def initialize_students():
    students.clear()
    students.extend(load_students())


def get_students():
    return students
