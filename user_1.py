import random
from subjects import Course
from department import Faculty, Major
from collections import defaultdict
class User:
    _username: str
    _password: str
    _role: str

    def __init__(self, username, password, role):
        self._username = username
        self._password = password
        self._role = role

    @property
    def password(self):
        return self._password

    @password.setter
    def password(self, password):
        self._password = password

class CourseDict(defaultdict):

    def __init__(self, **kwargs):
        super().__init__(int, **kwargs)

    def __setitem__(self, key, value):
        if not isinstance(key, Course):
            raise TypeError(f"Key must be of type Course")
        super().__setitem__(key, value)


class Student(User):
    id: str
    full_name: str
    major: Major
    faculty: Faculty
    courses: list
    _grades = CourseDict()

    def __init__(self, full_name, faculty: Faculty, major: Major, password):
        self.id = "S-" + faculty.id + "-" + major.id + "-" + str(random.randint(100, 999))
        super().__init__(self.id, password, "student")
        self.full_name = full_name
        self.major = major
        self.faculty = faculty
        self.courses = list()

    def _get_id(self):
        return self.id

    def _get_full_name(self):
        return self.full_name

    def _set_full_name(self, full_name):
        self.full_name = full_name

    def _get_major(self):
        return self.major

    def _set_major(self, major):
        self.major = major

    def _get_password(self):
        return self._password

    def get_courses(self):
        return self.courses

    def add_course(self, course):
        self.courses.append(course)

    def delete_course(self, course):
        self.courses.remove(course)

    def get_grades(self):
        return self._grades

    def set_grade(self, course, grade):
        self._grades[course] = grade


class Teacher(User):
    id: str
    full_name: str
    specialization: Course
    faculty: Faculty
    major: Major
    students: list

    def __init__(self, full_name, faculty: Faculty, major: Major, specialization: Course, password):
        self.id = "T-" + faculty.id + "-" + major.id + str(random.randint(100, 999))
        self.full_name = full_name
        self.faculty = faculty
        self.major = major
        self.specialization = specialization
        self.students = list()
        super().__init__(self.id, password, "teacher")

    def _get_id(self):
        return self.id

    def _get_password(self):
        return self._password

    def get_full_name(self):
        return self.full_name

    def set_full_name(self, full_name):
        self.full_name = full_name

    def get_specialization(self):
        return self.specialization.name

    def set_specialization(self, specialization):
        self.specialization = specialization

    def add_student(self, student):
        self.students.append(student)

    def delete_student(self, student):
        self.students.remove(student)



