class Student:

    def __init__(self, name, age):
        self.name = name
        self.__age = age

    @property
    def display_value(self):
        print(f"My name is {self.name}")

    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, value):
        if value >= 0:
            self.__age = value



st1 = Student("Sajib",23)

#without propert --> access display_value = display_value()
# st1.display_value()

#with property --> access display_value = display_value
st1.display_value


#access public value
# print(st1.age)

#access protectedValue
# print(st1._age)

#access private Value
st1.age = 34
print(st1.age)

