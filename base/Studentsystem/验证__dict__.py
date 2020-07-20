class A(object):
    a = 0

    def __init__(self):
        self.b = 1

aa = A()
print(A.__dict__)
print(aa.__dict__)
