class Student(object):
    """学员对象"""
    def __init__(self, name, gender, tel):
        self.name = name
        self.gender = gender
        self.tel = tel

    def __str__(self):
        return f'{self.name}, {self.gender}, {self.tel}'

# aa = Student('aa', 'man', '136********')
# print(aa)
