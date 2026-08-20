class MyDescriptor:

    def __get__(self, instance, owner):
        print("GET called")
        return instance._value

    def __set__(self, instance, value):
        print("SET called")
        instance._value = value


class Student:

    age = MyDescriptor()

    def __init__(self, age):
        self.age = age


student = Student(25)

print(student.age)

student.age = 30

print(student.age)