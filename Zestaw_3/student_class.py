class Student:
    def __init__(self, stud_name, marks_list):
        self.name = stud_name
        self.marks = marks_list

    def __str__(self):
        return f"{self.name}"

    def is_passed(self):
        marks_sum = 0
        for mark in self.marks:
            marks_sum += mark

        if (marks_sum / len(self.marks)) > 50:
            return True
        else:
            return False
