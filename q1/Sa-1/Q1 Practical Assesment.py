class AssignmentSubmission:
    def __init__(self, student_name, student_id, assignment_title, due_date, is_submitted=False, grade=None, submitted_files=None):
        self.student_name = student_name
        self.student_id = student_id
        self._assignment_title = assignment_title
        self._due_date = due_date
        self.__is_submitted = is_submitted
        self.__grade = grade
        self.__submitted_files = submitted_files if submitted_files is not None else []

    def validate_grade(self, score):
        return score >= 0

    def check_submission_status(self):
        return "Submitted" if self.__is_submitted else "Missing"

    def is_duplicate(self, filename):
        return filename in self.__submitted_files

    def add_file(self, filename):
        if self.is_duplicate(filename):
            print(f"--> [Warning] '{filename}' is already attached!")
        else:
            self.__submitted_files.append(filename)
            self.__is_submitted = True
            print(f"--> [Success] {self.student_name} attached '{filename}'. Total files: {len(self.__submitted_files)}")

    def remove_file(self, filename):
        if self.__grade is not None:
            print(f"--> [Warning] {self.student_name} cannot remove files. assignment already graded.")
            return
        if filename in self.__submitted_files:
            self.__submitted_files.remove(filename)
            print(f"--> [Success] {self.student_name} removed '{filename}'.")
            if not self.__submitted_files:
                self.__is_submitted = False
        else:
            print(f"--> [Error] File '{filename}' not found for {self.student_name}.")

    def assign_grade(self, score):
        if not self.__submitted_files:
            print(f"--> [Error] Cannot grade. No files submitted for {self.student_name}.")
            return
        if self.validate_grade(score):
            self.__grade = score
            print(f"--> [Success] Grade {score} officially assigned to {self.student_name}.")

    def get_grade(self):
        return self.__grade if self.__grade is not None else "No grade yet."

    def view_files(self):
        return ", ".join(self.__submitted_files) if self.__submitted_files else "No files submitted."

    def get_status_report(self):
        return f"ID : {self.student_id} | Name: {self.student_name} | Status: {self.check_submission_status()} ({len(self.__submitted_files)} files) | Grade: {self.get_grade()}"


print("--- INITIALIZING DROPBOX FOR STUDENTS ---\n")
student1 = AssignmentSubmission("Alex Gonzaga", "pshs-1090-x", "CS-101", "2026-10-01")
student2 = AssignmentSubmission("Adelle", "pshs-1920-x", "CS-103", "2026-10-01")
student3 = AssignmentSubmission("Juan dela Cruz", "pshs-1033-x", "CS-101", "2026-10-01")
student4 = AssignmentSubmission("Maria Santos", "pshs-1044-x", "CS-101", "2026-10-01")
student5 = AssignmentSubmission("Jose Reyes", "pshs-1055-x", "CS-101", "2026-10-01")

print("--- TEST SCENARIO 1: Multiple Files via List ---")
student1.add_file("main.py")
student1.add_file("report.pdf")
student1.assign_grade(95)
print(f"Alex's Files: {student1.view_files()}\n")

print("--- TEST SCENARIO 2: Removing Files from List ---")
student2.add_file("wrong_homework.docx")
student2.remove_file("wrong_homework.docx")
student2.add_file("correct_project.py")
student2.assign_grade(88)
print(f"Adelle's Files: {student2.view_files()}\n")

print("--- TEST SCENARIO 3: Preventing Duplicate Files ---")
student3.add_file("script.py")
student3.add_file("script.py")
print(f"Juan's Files: {student3.view_files()}\n")

print("--- TEST SCENARIO 4: Removing file after being graded ---")
student4.add_file("exam_answers.pdf")
student4.assign_grade(75)
student4.remove_file("exam_answers.pdf")
print(f"\n")

print("--- TEST SCENARIO 5: Empty List Handling ---")
student5.add_file("draft.txt")
student5.remove_file("draft.txt")
student5.assign_grade(100)
print(f"\n")

print("--- FINAL SYSTEM REPORT ---")
print(student1.get_status_report())
print(student2.get_status_report())
print(student3.get_status_report())
print(student4.get_status_report())
print(student5.get_status_report())
