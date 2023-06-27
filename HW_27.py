class GroupFullException(Exception):
    pass
class Human:

    def __init__(self, gender, age, first_name, last_name):
        self.gender = gender
        self.age = age
        self.first_name = first_name
        self.last_name = last_name

    def __str__(self):
        return f"Human [gender = {self.gender}, age = {self.age}, first_name = {self.first_name}, last_name = {self.last_name}]"


class Student(Human):

    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f"Student(Human) [gender = {self.gender}, age = {self.age}, first_name = {self.first_name}, last_name = {self.last_name}, record_book = {self.record_book}]"


class Group:
    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        if len(self.group) >= 10:
            print("The group is already full.")
        else:
            self.group.add(student)
        return self.group

    def find_student(self, last_name):
        for student in self.group:
            if student.last_name == last_name:
                return student
            else:
                return None

    def delete_student(self, last_name):
        student = self.find_student(last_name)
        if student:
            return self.group.pop()
        return None

    def __str__(self):
        all_students = "\n".join(str(student) for student in self.group)
        return f'Number:{self.number}\n {all_students}'

st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
st3 = Student('Female', 25, 'Ana', 'Novak', 'AN145')
st4 = Student('Female', 27, 'Diana', 'Ran', 'AN145')
st5 = Student('Male', 25, 'Ivan', 'Tor', 'AN145')
st6 = Student('Male', 31, 'Dylan', 'Mor', 'AN145')
st7 = Student('Male', 25, 'Jan', 'Ten', 'AN145')
st8 = Student('Female', 34, 'Bru', 'Len', 'AN145')
st9 = Student('Female', 32, 'Kirk', 'Dug', 'AN145')
st10 = Student('Female', 26, 'Mira', 'Yellow', 'AN145')
st11 = Student('Female', 26, 'Kira', 'Bum', 'AN145')
print(st1, st2, st3, st4, st5, st6, st7, st8, st9, st10, st11)
gr = Group('PD1')
gr.add_student(st1)
gr.add_student(st2)
gr.add_student(st3)
gr.add_student(st4)
gr.add_student(st5)
gr.add_student(st6)
gr.add_student(st7)
gr.add_student(st8)
gr.add_student(st9)
gr.add_student(st10)
gr.add_student(st11)
print(gr)
