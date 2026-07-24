from menu import show_menu
from services.student_service import (
    add_student,
    search_by_name,
    search_by_major,
    show_students,
    find_student,
    update_student,
    delete_student,
    save_data,
    load_data
)
from services.report_service import export_csv


def main():

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

        elif choice == "6":

            save_data()

        elif choice == "7":

            load_data()

        elif choice == "10":
            search_by_name()

        elif choice == "11":
            search_by_major()

        elif choice == "12":
            from services.student_service import students
            export_csv(students)
        elif choice == "0":

            print("Cảm ơn bạn đã sử dụng chương trình.")

            break

        else:

            print("Lựa chọn không hợp lệ.")


if __name__ == "__main__":
    main()