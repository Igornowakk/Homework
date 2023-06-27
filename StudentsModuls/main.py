import modul_student as student
import modul_group as group


st1 = student.Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = student.Student('Female', 25, 'Liza', 'Taylor', 'AN145')
gr = group.Group('PD1')
gr.add_student(st1)
gr.add_student(st2)
print(gr)
print(gr.find_student('Jobs'))  # 'Steve Jobs'
print(gr.find_student('Jobs2')) # None

gr.delete_student('Taylor')
print(gr) # Only one student
