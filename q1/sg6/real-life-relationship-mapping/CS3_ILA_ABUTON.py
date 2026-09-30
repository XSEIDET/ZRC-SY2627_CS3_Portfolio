
class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id


class Course:
    def __init__(self, course_name):
        self.course_name = course_name
        self.students = []

    def add_student(self, student):
        self.students.append(student)



math = Course("Mathematics")


student1 = Student("Rossweisee", 1)
student2 = Student("Dalleto", 2)
student3 = Student("Ava", 3)


math.add_student(student1)
math.add_student(student2)
math.add_student(student3)


print("Course:", math.course_name)
print("Students enrolled:")

for student in math.students:
    print(student.name, "-", student.student_id)