def is_duplicate_id(students, student_id):
    return any(s.student_id == student_id for s in students)


def is_valid_age(age): return age > 0
def is_valid_name(name): return len(name.strip()) > 0
def is_valid_major(major): return len(major.strip()) > 0
def is_valid_score(score): return 0 <= score <= 10


def input_score(subject, current=None):

    while True:

        text = f"Điểm {subject}"

        if current is not None:
            text += f" [{current}]"

        text += ": "

        value = input(text).strip()

        if value == "" and current is not None:
            return current

        try:
            score = float(value)

            if is_valid_score(score):
                return score

            print("Điểm phải từ 0 đến 10.")

        except ValueError:
            print("Vui lòng nhập số.")
