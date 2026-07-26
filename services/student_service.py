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
students = load_students()


# ==========================
# Thêm sinh viên
# ==========================
def add_student():

    print("\n===== THÊM SINH VIÊN =====")

    student_id = input("Mã sinh viên: ")

    if is_duplicate_id(students, student_id):
        print(">> Mã sinh viên đã tồn tại.")
        return

    name = input("Họ tên: ")

    if not is_valid_name(name):
        print(">> Họ tên không hợp lệ.")
        return

    try:
        age = int(input("Tuổi: "))
    except ValueError:
        print(">> Tuổi phải là số.")
        return

    if not is_valid_age(age):
        print(">> Tuổi phải lớn hơn 0.")
        return

    major = input("Ngành học: ")

    if not is_valid_major(major):
        print(">> Ngành học không hợp lệ.")
        return
    math=input_score("Toán")
    literature=input_score("Văn")
    english=input_score("Anh")
    student = Student(
        student_id,
        name,
        age,
        major,
        math,
        literature,
        english
    )

    students.append(student)
    save_students(students)
    logger.info(f"Thêm sinh viên: {student.student_id} - {student.name}")
    print("\n>> Thêm sinh viên thành công.")
# ==========================
# Hiển thị danh sách
# ==========================


def show_students():
    print("\n===== DANH SÁCH SINH VIÊN =====")

    if len(students) == 0:
        print("Danh sách rỗng.")
        return

    for student in students:
        student.display()


# ==========================
# Tìm kiếm sinh viên
# ==========================
def find_student():
    print("\n===== TÌM KIẾM SINH VIÊN =====")

    student_id = input("Nhập mã sinh viên: ")

    for student in students:
        if student.student_id == student_id:
            print("\nĐã tìm thấy sinh viên:")
            student.display()
            return

    print("Không tìm thấy sinh viên.")


# ==========================
# Cập nhật sinh viên
# ==========================
def update_student():

    print("\n===== CẬP NHẬT SINH VIÊN =====")

    student_id = input("Nhập mã sinh viên: ")

    for student in students:

        if student.student_id == student_id:

            name = input("Tên mới: ")

            if not is_valid_name(name):
                print("Tên không hợp lệ.")
                return

            try:
                age = int(input("Tuổi mới: "))
            except ValueError:
                print("Tuổi phải là số.")
                return

            if not is_valid_age(age):
                print("Tuổi phải lớn hơn 0.")
                return

            major = input("Ngành mới: ")

            if not is_valid_major(major):
                print("Ngành không hợp lệ.")
                return

            student.name = name
            student.age = age
            student.major = major
            m=input(f"Điểm Toán [{student.math}]: ")
            if m.strip(): student.math=float(m)
            l=input(f"Điểm Văn [{student.literature}]: ")
            if l.strip(): student.literature=float(l)
            e=input(f"Điểm Anh [{student.english}]: ")
            if e.strip(): student.english=float(e)
            save_students(students)
            logger.info(f"Cập nhật sinh viên: {student.student_id}")
            print("\n>> Cập nhật thành công.")
            return

    print("Không tìm thấy sinh viên.")

# ==========================
# Xóa sinh viên
# ==========================


def delete_student():
    print("\n===== XÓA SINH VIÊN =====")

    student_id = input("Nhập mã sinh viên cần xóa: ")

    for student in students:
        if student.student_id == student_id:

            print("\nThông tin sinh viên:")
            student.display()

            confirm = input("Bạn có chắc muốn xóa? (Y/N): ")

            if confirm.upper() == "Y":
                students.remove(student)
                save_students(students)
                logger.info(f"Xóa sinh viên: {student.student_id}")
                print("\n>> Xóa sinh viên thành công!")
            else:
                print("\n>> Đã hủy xóa.")

            return

    print("\nKhông tìm thấy sinh viên.")


def save_data():
    save_students(students)


def load_data():
    global students
    students = load_students()
    print("Đã đọc dữ liệu thành công.")


def search_by_name():

    keyword = input("Nhập tên cần tìm: ").lower()

    found = False

    for student in students:

        if keyword in student.name.lower():
            student.display()
            found = True

    if not found:
        print("Không tìm thấy.")


def search_by_major():

    keyword = input("Nhập ngành: ").lower()

    found = False

    for student in students:

        if keyword in student.major.lower():
            student.display()
            found = True

    if not found:
        print("Không tìm thấy.")


def statistic():
    counts={"Giỏi":0,"Khá":0,"Trung bình":0,"Yếu":0}
    for s in students: counts[s.classification()]+=1
    for k,v in counts.items(): print(f"{k}: {v}")

def sort_gpa():
    for s in sorted(students,key=lambda x:x.average_score(),reverse=True):
        s.display()
