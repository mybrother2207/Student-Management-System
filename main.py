from menu import show_menu
from services.student_service import initialize_students
from services.student_service import students


from services.student_service import (
    add_student,
    search_by_name,
    search_by_major,
    show_students,
    find_student,
    update_student,
    delete_student,
    statistic,
    sort_gpa
)
from services.report_service import export_excel


def main():

    initialize_students()

    while True:

        show_menu()

        choice = input("Nhập lựa chọn: ")

        if choice == "1":

            add_student()

        elif choice == "2":

            show_students()

        elif choice == "3":
            
            find_student()

        elif choice == "4":

            update_student()

        elif choice == "5":

            delete_student()

        elif choice == "8":
            statistic()

        elif choice == "9":
            sort_gpa()

        elif choice == "10":
            search_by_name()

        elif choice == "11":
            search_by_major()

        elif choice == "12":
            export_excel(students)
        elif choice == "0":

            print("Cảm ơn bạn đã sử dụng chương trình.")

            break

        else:

            print("Lựa chọn không hợp lệ.")


if __name__ == "__main__":
    main()
