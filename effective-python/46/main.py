class Grade:
    def __init__(self):
        self._values = {}

    def __get__(self, instance, instance_type):
        if instance is None:
            return self
        return self._values.get(instance, 0)

    def __set__(self, instance, value):
        if not (0 <= value <= 100):
            raise ValueError("Grade must be between 0 and 100")
        self._values[instance] = value


class Exam:
    math_grade = Grade()
    writing_grade = Grade()
    science_grade = Grade()


first_exam = Exam()
first_exam.writing_grade = 83
first_exam.science_grade = 75
print(first_exam.writing_grade)
print(first_exam.science_grade)

secound_exam = Exam()
print(secound_exam.writing_grade)
print(secound_exam.science_grade)
