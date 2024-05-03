class Course:
    _code: str
    _name: str

    def __init__(self, code, name):
        self.code = code
        self.name = name

    def get_code(self):
        return self._code

    def get_name(self):
        return self._name

