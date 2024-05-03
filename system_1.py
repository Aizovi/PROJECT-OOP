from department import *
from user import Student, Teacher
from subjects import Course
class SIS:
    courses: dict
    users: dict
    subjects = {
        "1": {"1": (
                Course("CAB-100", "Biology"),
                Course("CAB-200", "Chemistry"),
                Course("CAB-300", "Anatomy")),
            "2": (
                Course("TFL-100", "English"),
                Course("TFL-200", "French"),
                Course("TFL-300", "Turkish")),
            "3": (
                Course("PI-100", "Physics"),
                Course("PI-200", "Informatics"),
                Course("PI-300", "Pedagogy"))},

        "2": {"1": (
                Course("CSS-100", "Programming"),
                Course("CSS-200", "Algorithms"),
                Course("CSS-300", "Python")),
            "2": (
                Course("ISS-100", "ICT"),
                Course("ISS-200", "Java"),
                Course("ISS-300", "BackEnd")),
            "3": (
                Course("MSS-100", "Design"),
                Course("MSS-200", "3D Modeling"),
                Course("MSS-300", "Blender"))},

        "3": {"1": (
                Course("MNG-100", "Product Management"),
                Course("MNG-200", "Project Management"),
                Course("MNG-300", "Management Basics")),
            "2": (
                Course("MKG-100", "Marketing Basis"),
                Course("MKG-200", "Customer Analyze"),
                Course("MKG-300", "Marketing Methods")),
            "3": (
                Course("ACC-100", "Data Science"),
                Course("ACC-200", "Finance"),
                Course("ACC-300", "Investment"))}
            }

    majors = {"1": [
            Major("1", "Chemistry and Biology"),
            Major("2", "Two Foreign Languages"),
            Major("3", "Physics Informatics")],
        "2": [
            Major("1", "Computer Science"),
            Major("2", "Information Systems"),
            Major("3", "Multimedia Sciences")],
        "3": [
            Major("1", "Management"),
            Major("2", "Marketing"),
            Major("3", "Accounting")]}

    faculties = (
        Faculty("1", "Education and Humanities", majors["1"]),
        Faculty("2", "Engineering and Natural Science", majors["2"]),
        Faculty("3", "Business School", majors["3"]))


    def __init__(self, users, courses):
        self.courses = courses
        self.users = users


    def register_student(self, full_name, faculty, major, password):
        new_student = Student(full_name, faculty, major, password)
        self.users[new_student.id] = new_student
        return new_student.id

    def register_teacher(self, full_name, faculty, major, course, password):
        new_teacher = Teacher(full_name, faculty, major, course, password)
        self.users[new_teacher.id] = new_teacher
        self.courses[course.code] = new_teacher
        return new_teacher.id

    def student_add_course(self, student, course):
        teacher = self.courses.get(course.code)
        if teacher:
            student.add_course(course)
            teacher.add_student(student)
            print("""
=====================
Added:
{} : {} --> {}
=====================""".format(course.code, course.name, teacher.full_name))
        else:
            print("""
===============================            
This course has no teacher yet!
===============================""")

    def student_delete_course(self, student, course):
        student.delete_course(course)
        teacher = self.courses.get(course.code)
        teacher.delete_student(student)
        print("""
======================
Successfully Deleted:
{} : {} --> {}
======================""".format(course.code, course.name, teacher.full_name))

    def change_password(self, user, password):
        user.password = password
        print("""
            ==================
            New Password: {}
            ==================""".format(password))