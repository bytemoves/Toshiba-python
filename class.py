class Student:
    def __init__(self, name, course, gender, age):
        self.name = name
        self.course = course
        self.gender = gender
        self.age = age

    def darasa(self):
        print("name: %s\ncourse: %s\ngender: %s\nage: %d" % (self.name, self.course, self.gender, self.age))

std1 = Student("erick", "computer science", "male", 20)
std1.darasa()
std2 = Student("kuria", "computer science", "female", 19)
std2.darasa()
std3 = Student("ann", "software engineering", "female", 19)
std3.darasa()
std4 = Student("liam", "software engineering", "male", 20)
std4.darasa()
