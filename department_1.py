from subjects import Course

class Major:
    _id: str
    _name: str
    description: str
    courses = set()

    def __init__(self, id, name):
        self._id = id
        self._name = name

    def get_courses(self):
        for course in self.courses:
            print("{}\t{}".format(course.code, course.name))

    def add_course(self, course: Course):
        self.courses.add(course)

    def get_id(self):
        return self._id

    def get_name(self):
        return self._name

    def get_description(self):
        return self.description

    id = property(get_id)
    name = property(get_name)
    description = property(get_description)

class Faculty:
    _id: str
    _name: str
    majors = set()

    def __init__(self, id, name, majors):
        self._id = id
        self._name = name
        self.majors = majors

    def get_majors(self):
        for major in self.majors:
            print("{}\n{}".format(major.name, major.description))

    def add_major(self, major: Major):
        self.majors.add(major)

    def get_id(self):
        return self._id

    def get_name(self):
        return self._name

    id = property(get_id)
    name = property(get_name)
