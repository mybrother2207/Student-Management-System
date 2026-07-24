def is_duplicate_id(students, student_id):
    for student in students:
        if student.student_id == student_id:
            return True
    return False


def is_valid_age(age):
    return age > 0


def is_valid_name(name):
    return len(name.strip()) > 0


def is_valid_major(major):
    return len(major.strip()) > 0