import pickle
from system import SIS
from user import Student, Teacher
class Menu:
    def __init__(self):
        self.system = SIS()
        self.choices = {"1": self.log_in, "2": self.sign_in}
        self.student_choices = {
                "1": self.student_info,
                "2": self.course_grades,
                "3": self.add_course,
                "4": self.delete_course,
                "5": self.change_password}
        self.teacher_choices = {
            "1": self.teacher_info,
            "2": self.set_grade,
            "3": self.change_password}


    def display_menu(self):
        print("""
--------------------------
Information System Service
--------------------------
1. Log In
2. Sign Up
0. Exit
""")

    def run(self):
        print("Welcome to Information System Service")
        while True:
            self.display_menu()
            choice = input("Enter an option: ")
            if choice == "0":
                with open("users.pkl", 'wb') as users_file:
                    pickle.dump(self.system.users, users_file)
                with open("courses.pkl", 'wb') as courses_file:
                    pickle.dump(self.system.courses, courses_file)
                return
            action = self.choices.get(choice)
            if action:
                action()
            else:
                print("\n{0} is not a valid choice".format(choice))

    def sign_in(self):
        while True:
            print("""
------------
Registration
------------
1. Student
2. Teacher
0. Exit
""")

            role = input("Select your role: ")
            if role == "1":
                self.student_sign_in()
                break
            elif role == "2":
                self.teacher_sign_in()
                break
            elif role == "0":
                break
            else:
                print("{0} is not a valid choice".format(role))

    def student_sign_in(self):
        print("""
--------------------
Student Registration
-------------------- """)
        full_name = input("Enter your full name: ")
        print("---------------------")
        print("Faculties: ")
        for faculty in self.system.faculties:
            print("{}. {}".format(faculty.id, faculty.name))
        faculty_id = input("Enter your faculty: ")
        faculty = self.system.faculties[int(faculty_id) - 1]
        print("---------------------")
        print("Majors: ")
        for major in self.system.majors[faculty_id]:
            print("{}. {}".format(major.id, major.name))
        major_id = input("Enter your major: ")
        major = self.system.majors[faculty_id][int(major_id) - 1]
        print("---------------------")
        password = input("Enter your password: ")

        new_student_id = self.system.register_student(full_name, faculty, major, password)

        print("""
=====================
Your ID: {}
Your password: {} 
===================== """.format(new_student_id, password))

    def teacher_sign_in(self):
        print("""
--------------------
Teacher Registration
-------------------- """)
        full_name = input("Enter your full name: ")
        print("---------------------")
        print("Faculties: ")
        for faculty in self.system.faculties:
            print("{}. {}".format(faculty.id, faculty.name))
        faculty_id = input("Enter your faculty: ")
        faculty = self.system.faculties[int(faculty_id) - 1]
        print("---------------------")
        print("Majors: ")
        for major in self.system.majors[faculty_id]:
            print("{}. {}".format(major.id, major.name))
        major_id = input("Enter your major: ")
        major = self.system.majors[faculty_id][int(major_id) - 1]
        print("---------------------")
        print("Courses: ")
        index = 1
        for course in self.system.subjects[faculty_id][major_id]:
            print("{}. {} - {}".format(index, course.code, course.name))
            index += 1
        course_id = input("Enter your course: ")
        course = self.system.subjects[faculty_id][major_id][int(course_id) - 1]
        print("---------------------")
        password = input("Enter your password: ")

        new_teacher_id = self.system.register_teacher(full_name, faculty, major, course, password)

        print("""
=====================
Your ID: {}
Your password: {} 
===================== """.format(new_teacher_id, password))


    def log_in(self):
        while True:
            id = input("Enter your ID: ")
            password = input("Enter your password: ")
            user = self.system.users.get(id)
            incorrect_message = """
==================
Incorrect Password
=================="""
            if user:
                if isinstance(user, Student):
                    self.student_menu(user) if password == user.password else print(incorrect_message)
                    break
                elif isinstance(user, Teacher):
                    self.teacher_menu(user) if password == user.password else print(incorrect_message)
                    break
            else:
                print("\nNO SUCH USER EXISTS")
                break


    def display_student_menu(self):
        print("""
--------------------
Student Menu
-------------------- 
1. My Info
2. Course Grades
3. Add Course
4. Delete Course
5. Change Password
0. Exit
""")

    #STUDENT MENU
    def student_menu(self, student):
        print("\nWelcome, {}".format(student.full_name))
        while True:
            self.display_student_menu()
            choice = input("Enter an option: ")
            if choice == "0":
                break
            student_action = self.student_choices.get(choice)
            if student_action:
                student_action(student)
            else:
                print("\n{0} is not a valid choice".format(choice))

    #1. MY INFO(STUDENT)
    def student_info(self, student):
        print("""
==================
ID: {}
Full Name: {}
Faculty: {}
Major: {}
==================""".format(student.id, student.full_name, student.faculty.name, student.major.name))

    #2. COURSE GRADES
    def course_grades(self, student):
        if len(student.courses) == 0:
            print("""
===============================
THERE IS NO COURSE IN YOUR LIST
===============================""")
            return
        index = 1
        grades = student.get_grades()
        print("""
=============================
    CODE     NAME       GRADE""")
        for course in student.get_courses():
            print("{}.  {}   {}    {}".format(index,
                                                   course.code, course.name, grades[course]))
            index += 1
        print("=============================")

    #3. ADD COURSE(STUDENT)
    def add_course(self, student):
        courses = self.system.subjects[student.faculty.id][student.major.id]
        index = 1
        for course in courses:
            print("{}. {} - {}".format(index, course.code, course.name))
            index += 1
        choice = input("Enter course: ")
        course = self.system.subjects[student.faculty.id][student.major.id][int(choice) - 1]
        if course in student.get_courses():
            print("""
====================================
You have already chosen this course!
====================================""")
        else:
            self.system.student_add_course(student, course)

    #4. DELETE COURSE(STUDENT)
    def delete_course(self, student):
        if len(student.courses) == 0:
            print("""
===============================
THERE IS NO COURSE IN YOUR LIST
===============================""")
            return
        index = 1
        for course in student.get_courses():
            print("{}. {} - {}".format(index, course.code, course.name))
            index += 1
        try:
            choice = int(input("Enter course: "))
            course = student.courses[choice - 1]
            self.system.student_delete_course(student, course)
        except IndexError:
            print("\nInvalid input. Please select a valid course number.")
        except ValueError:
            print("\nInvalid input. Please enter a number.")

    def display_teacher_menu(self):
        print("""
--------------------
Teacher Menu
-------------------- 
1. My Info
2. Student Grade
3. Change Password
0. Exit""")


    def teacher_menu(self, teacher):
        print("""
====================
Welcome, {} teacher!
====================""".format(teacher.full_name))
        while True:
            self.display_teacher_menu()
            choice = input("Enter an option: ")
            if choice == "0":
                break
            teacher_action = self.teacher_choices.get(choice)
            if teacher_action:
                teacher_action(teacher)
            else:
                print("\n{0} is not a valid choice".format(choice))

    #MY INFO(TEACHER)
    def teacher_info(self, teacher):
        print("""
==================
ID: {}
Full Name: {}
Faculty: {}
Major: {}
Course: {} - {}
==================""".format(teacher.id, teacher.full_name, teacher.faculty.name,
        teacher.major.name, teacher.specialization.code, teacher.specialization.name))

    #2. STUDENT GRADE
    def set_grade(self, teacher):
        if len(teacher.students) == 0:
            print("""
=========================
You have no students yet!
=========================""")
            return

        index = 1
        course = teacher.specialization
        print("""
==================================
   ID         NAME           GRADE""")
        for student in teacher.students:
            print("{}. {}  {}  {}".format(index, student.id,
                                          student.full_name, student.get_grades()[course]))
        print("==================================")
        student_index = int(input("Choose student: "))
        student = teacher.students[student_index - 1]
        grade = int(input("Set your grade(1-5): "))
        student.set_grade(teacher.specialization, grade)

    #CHANGE USER PASSWORD
    def change_password(self, user):
        print("""
----------------
Reset Password
----------------""")
        password = input("Enter new password: ")
        self.system.change_password(user, password)


if __name__ == '__main__':
    with open("users.pkl", 'rb') as users_file:
        try:
            users = pickle.load(users_file)
        except EOFError:
            users = dict()
    with open("courses.pkl", 'rb') as courses_file:
        try:
            courses = pickle.load(courses_file)
        except EOFError:
            courses = dict()
    m = Menu()
    m.run()

