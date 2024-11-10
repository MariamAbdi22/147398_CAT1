#Online Course Management System
class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.assignments = {}

    #Adding an assignment and the grade
    def add_assignment(self, assignment_name, grade):
        self.assignments[assignment_name] = grade
        print(f"Added assignment '{assignment_name}' with grade {grade} for {self.name}")

    #Displaying all grades
    def display_grades(self):
        if not self.assignments:
            print(f"{self.name} has no grades")
        else:
            print(f"Grades for {self.name}:")
            for assignment, grade in self.assignments.items():
                print(f"{assignment}: {grade}")


#Defining the instructor class
class Instructor:
    def __init__(self, name, course_name):
        self.name = name
        self.course_name = course_name
        self.students = []

    #Adding students to the course
    def add_student(self, student):
        self.students.append(student)
        print(f"Added student '{student.name}' to {self.course_name}.")

    #Asigning a grade to a student
    def assign_grade(self, student_id, assignment_name, grade):
        student = next((s for s in self.students if s.student_id == student_id), None)
        if student:
            student.add_assignment(assignment_name, grade)
        else:
            print(f"Student '{student_id}' not found.")

    #Displaying all students and their grades
    def display_students_and_grades(self):
        print(f"Grades for all students in the course: {self.course_name}")
        for student in self.students:
            student.display_grades()

    #Interactive code to allow an instructor to add students and assign grades
    def interactive_mode(self):
        while True:
            print("\nOptions:")
            print("1. Add a new student")
            print("2. Assign a grade to a student")
            print("3. Display all students and their grades")
            print("4. Exit")
            choice = input("Enter your choice (1-4): ")

            if choice == "1":
                name = input("Enter student's name: ")
                student_id = input("Enter student id: ")
                student = Student(name, student_id)
                self.add_student(student)

            elif choice == "2":
                student_id = input("Enter student id: ")
                assignment_name = input("Enter assignment name: ")
                grade = float(input("Enter grade: "))
                self.assign_grade(student_id, assignment_name, grade)


            elif choice == "3":
                self.display_students_and_grades()

            elif choice == "4":
                print("Thank you!")
                break

            else:
                print("Invalid choice. Please try again.")

instructor = Instructor("<NAME>", "HP")
instructor.interactive_mode()





