# ==========================================
# Parent class
# ==========================================

class Animal:

    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating")

    def sound(self):
        print("Animal makes a sound")


# ==========================================
# 1. SINGLE INHERITANCE
# Dog inherits from Animal
# ==========================================

class Dog(Animal):

    def sound(self):
        print("Dog says: Woof")


# ==========================================
# 2. MULTILEVEL INHERITANCE
# Puppy inherits from Dog
# Dog inherits from Animal
# ==========================================

class Puppy(Dog):

    def play(self):
        print(f"{self.name} is playing")


# ==========================================
# 3. HIERARCHICAL INHERITANCE
# Cat and Bird both inherit from Animal
# ==========================================

class Cat(Animal):

    def sound(self):
        print("Cat says: Meow")


class Bird(Animal):

    def sound(self):
        print("Bird says: Chirp")


# ==========================================
# 4. MULTIPLE INHERITANCE
# A class inherits from more than one parent
# ==========================================

class Swimmer:

    def swim(self):
        print("Swimming")


class Flyer:

    def fly(self):
        print("Flying")


class Duck(Animal, Swimmer, Flyer):

    def sound(self):
        print("Duck says: Quack")


# ==========================================
# 5. HYBRID INHERITANCE
# Combination of different inheritance types
# ==========================================

class FlyingDog(Dog, Flyer):

    def fly(self):
        print(f"{self.name} can fly")


# ==========================================
# Create objects
# ==========================================

dog = Dog("Tommy")
puppy = Puppy("Rocky")
cat = Cat("Mimi")
bird = Bird("Tweety")
duck = Duck("Donald")
flying_dog = FlyingDog("SuperDog")


# ==========================================
# SINGLE INHERITANCE
# ==========================================

print("----- Dog -----")

dog.eat()       # From Animal
dog.sound()     # Dog's own version


# ==========================================
# MULTILEVEL INHERITANCE
# ==========================================

print("\n----- Puppy -----")

puppy.eat()     # From Animal
puppy.sound()   # From Dog
puppy.play()    # From Puppy


# ==========================================
# HIERARCHICAL INHERITANCE
# ==========================================

print("\n----- Cat -----")

cat.eat()       # From Animal
cat.sound()     # Cat's version


print("\n----- Bird -----")

bird.eat()      # From Animal
bird.sound()    # Bird's version


# ==========================================
# MULTIPLE INHERITANCE
# ==========================================

print("\n----- Duck -----")

duck.eat()      # From Animal
duck.swim()     # From Swimmer
duck.fly()      # From Flyer
duck.sound()    # Duck's version


# ==========================================
# HYBRID INHERITANCE
# ==========================================

print("\n----- Flying Dog -----")

flying_dog.eat()        # From Animal
flying_dog.sound()      # From Dog
flying_dog.fly()        # From Flyer
flying_dog.fly()        # FlyingDog's method


# ==========================================
# isinstance()
# ==========================================

print("\n----- isinstance() -----")

print(isinstance(dog, Dog))
print(isinstance(dog, Animal))
print(isinstance(puppy, Animal))
print(isinstance(duck, Swimmer))


# ==========================================
# issubclass()
# ==========================================

print("\n----- issubclass() -----")

print(issubclass(Dog, Animal))
print(issubclass(Puppy, Dog))
print(issubclass(Puppy, Animal))
print(issubclass(Duck, Swimmer))


# ==========================================
# MRO
# ==========================================

print("\n----- MRO -----")

print(Duck.mro())
print(FlyingDog.mro())