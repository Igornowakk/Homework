
class Group:
    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        self.group.add(student)
        return self.group

    def delete_student(self, student):
        for student in self.group:
            if student.last_name in self.group:
                return self.group.pop(student)

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
            else:
                return None

    def __str__(self):
        all_students = "\n".join(str(student) for student in self.group)
        return f'Number:{self.number}\n {all_students}'