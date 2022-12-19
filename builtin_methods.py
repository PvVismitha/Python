"""
This class shows the builtin methods usage
python supports basic operations on objects like add, len, etc through dunder methods

"""


class Student:
    def __init__(self, name, marks, age, gender):
        self.name = name
        self.marks = marks
        self.age = age
        self.gender = gender

    def __repr__(self):
        return f'Student({self.name}, {self.marks}, {self.age}, {self.gender})'

    def __add__(self, other):
        return self.marks + other.marks


ravi = Student(name='Ravi', marks=123, age=12, gender='M')
ram = Student(name='Ram', marks=183, age=12, gender='M')
print(ravi)
print(ram)
total_marks = ravi + ram
print(f"Total marks score by ravi and ram are: {total_marks}")
