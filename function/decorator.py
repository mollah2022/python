def decorator(func):
    def wrapper():
        print("Starting Code")
        func()
        print("Ending Code")

    return wrapper

def say_hello():
    print("Hello W3 kids")

callback = decorator(say_hello)
callback()


def decorator(func):

    def wrapper():
        print("Start")
        func()
        print("End")

    return wrapper


@decorator
def hello():
    print("Hello")


hello()

@decorator
def display():
    print("Good Moring")

display()

@decorator
def update():
    print("Hello everyone")

update()


def decorator(func):

    def wrapper(*args, ** kwargs):
        print("Start")
        result = func(*args, **kwargs)
        print("End")

        return result

    return wrapper

@decorator
def add( a, b):
    return a + b

result = add(10,20)
print(result)



import time
from functools import wraps


def timer(func):

    @wraps(func)
    def wrapper(*args, **kwargs):

        start = time.time()

        result = func(*args, **kwargs)

        end = time.time()

        print("Time:", end - start)

        return result

    return wrapper


@timer
def calculate():
    total = 0

    for i in range(1000000):
        total += i

    return total

calculate()