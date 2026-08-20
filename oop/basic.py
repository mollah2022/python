class Student:

    #class attribute
    university = "BUBT"

    #constructor
    def __init__(self, name, age):
        #Instance attribute
        self.name = name
        self.age = age

    #Instance method
    def introduce(self):
        print(f"My name is {self.name}")
        print(f"My name is {self.age}")

    
    #class method
    @classmethod
    def show_university(cls):
        print(f"University: {cls.university}")

    #static method
    @staticmethod
    def is_adult(age):
        return age >= 18

#object
student1 = Student("Sajib", 25)

# Instance method
student1.introduce()

# class attribute
print(student1.university)

# class method
Student.show_university()

# static method
print(Student.is_adult(25))