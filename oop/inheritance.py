class Animal:

    def __init__(self,name):
        self.name = name
    
    def sound(self):
        print("Animal make a sound")

    
class Dog(Animal):
    def __init__(self ,name, age):
        super().__init__(name)
        self.age = age
    
    def sound(self):
        super().sound()
        print(f"This is a {self.name} and {self.name} are {self.age} year old")

dog1 = Dog("Dog",24)
dog1.sound()



class Animal:

    def __init__(self, name):
        self.name = name

    def sound(self):
        print("Animal makes a sound")

    def eat(self):
        print(f"{self.name} is eating")


class Dog(Animal):

    def __init__(self, name, breed):
        super().__init__(name)
        self.breed = breed

    def sound(self):
        print("Dog says: Woof")


dog = Dog("Tommy", "Labrador")

dog.eat()
dog.sound()

print(isinstance(dog, Dog))
print(isinstance(dog, Animal))

print(issubclass(Dog, Animal))
