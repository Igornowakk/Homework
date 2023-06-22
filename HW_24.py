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


st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
print(st1, st2)
gr = Group('PD1')
gr.add_student(st1)
gr.add_student(st2)
print(gr)
print(gr.find_student('Jobs'))   # 'Steve Jobs'
print(gr.find_student('Kobs2'))  # None

gr.delete_student('Taylor')
print(gr) # Only one student
