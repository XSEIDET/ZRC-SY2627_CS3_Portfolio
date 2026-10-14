
class CD:
    def __init__(self, director):
        self.__director = director

    @property
    def director(self):
        return self.__director

    @director.setter
    def director(self, value):
        self.__director = value

    def show_director(self):
        print("Campus Director:", self.director)

    def show_campus(self):
        print("Campus: Zamboanga Peninsula Regional Campus")


class CID(CD):
    def __init__(self, director, head, curriculum, year, subjects):
        super().__init__(director)
        self.__head = head
        self.__curriculum = curriculum
        self.__year = year
        self.__subjects = subjects

    @property
    def head(self):
        return self.__head

    @head.setter
    def head(self, value):
        self.__head = value

    @property
    def curriculum(self):
        return self.__curriculum

    @curriculum.setter
    def curriculum(self, value):
        self.__curriculum = value

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, value):
        self.__year = value

    @property
    def subjects(self):
        return self.__subjects

    @subjects.setter
    def subjects(self, value):
        self.__subjects = value

    def show_cid(self):
        print("CID Head:", self.head)
        print("Curriculum:", self.curriculum)

    def check_subjects(self):
        print("Number of Subjects:", self.subjects)


class SSD(CD):
    def __init__(self, director, head, service):
        super().__init__(director)
        self.__head = head
        self.__service = service

    @property
    def head(self):
        return self.__head

    @head.setter
    def head(self, value):
        self.__head = value

    @property
    def service(self):
        return self.__service

    @service.setter
    def service(self, value):
        self.__service = value

    def show_ssd(self):
        print("SSD Head:", self.head)

    def help_students(self):
        print("Service:", self.service)


class Academic(CID):
    def __init__(self, director, head, curriculum, year,
                 subjects, department):
        super().__init__(director, head, curriculum, year, subjects)
        self.__department = department

    @property
    def department(self):
        return self.__department

    @department.setter
    def department(self, value):
        self.__department = value

    def show_department(self):
        print("Department:", self.department)


class Assessment(CID):
    def __init__(self, director, head, curriculum, year,
                 subjects, assessment):
        super().__init__(director, head, curriculum, year, subjects)
        self.__assessment = assessment

    @property
    def assessment(self):
        return self.__assessment

    @assessment.setter
    def assessment(self, value):
        self.__assessment = value

    def show_assessment(self):
        print("Assessment:", self.assessment)


class Examination(Assessment):
    def __init__(self, director, head, curriculum, year,
                 subjects, assessment, schedule):
        super().__init__(
            director, head, curriculum, year, subjects, assessment
        )
        self.__schedule = schedule

    @property
    def schedule(self):
        return self.__schedule

    @schedule.setter
    def schedule(self, value):
        self.__schedule = value

    def show_schedule(self):
        print("Exam Schedule:", self.schedule)


class Faculty(CID):
    def __init__(self, director, head, curriculum, year,
                 subjects, training):
        super().__init__(director, head, curriculum, year, subjects)
        self.__training = training

    @property
    def training(self):
        return self.__training

    @training.setter
    def training(self, value):
        self.__training = value

    def show_training(self):
        print("Training:", self.training)


class StudentWelfare(SSD):
    def __init__(self, director, head, service, program):
        super().__init__(director, head, service)
        self.__program = program

    @property
    def program(self):
        return self.__program

    @program.setter
    def program(self, value):
        self.__program = value

    def show_program(self):
        print("Welfare Program:", self.program)


# Creating objects

cd = CD("Sir Gallamaso")
cid = CID("Sir Gallamaso", "Ma'am Raznee",
          "K-12 Curriculum", "2026-2027", 8)
ssd = SSD("Sir Gallamaso", "Gamil", "Student Counseling")

academic = Academic("Sir Gallamaso", "Ma'am Raznee",
                    "K-12 Curriculum", "2026-2027", 8, "Science")

assessment = Assessment("Sir Gallamaso", "Ma'am Raznee",
                        "K-12 Curriculum", "2026-2027", 8,
                        "Quarterly Exam")

exam = Examination("Sir Gallamaso", "Ma'am Raznee",
                   "K-12 Curriculum", "2026-2027", 8,
                   "Quarterly Exam", "October 20")

faculty = Faculty("Sir Gallamaso", "Ma'am Raznee",
                  "K-12 Curriculum", "2026-2027", 8,
                  "Teacher Training")

welfare = StudentWelfare("Sir Gallamaso", "Gamil",
                         "Student Counseling", "Student Wellness")


# Displaying information

print("=== CAMPUS DIRECTOR ===")
cd.show_director()
cd.show_campus()

print("\n=== CID ===")
cid.show_director()
cid.show_cid()
cid.check_subjects()

print("\n=== SSD ===")
ssd.show_director()
ssd.show_ssd()
ssd.help_students()

print("\n=== ACADEMIC ===")
academic.show_cid()
academic.show_department()

print("\n=== ASSESSMENT ===")
assessment.show_cid()
assessment.show_assessment()

print("\n=== EXAMINATION ===")
exam.show_assessment()
exam.show_schedule()

print("\n=== FACULTY ===")
faculty.show_cid()
faculty.show_training()

print("\n=== STUDENT WELFARE ===")
welfare.show_ssd()
welfare.show_program()
