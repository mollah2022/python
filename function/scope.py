def apply_operation(func, value):
    return func(value)

def double(x):
    return x * 2

print(apply_operation(double, 5))  # Output: 10



def cal(a,b):
    return a + b

x = cal
print(x(10,20))


def add(a, b):
    return a + b


def calculate(func, x, y):
    return func(x, y)


result = calculate(add, 10, 20)

print(result)



def outerfunctio(func):
    def inner():
        print("starting")
        func()
        print("ending")

    return inner


def display():
    print("Welcome our website....")

hello = outerfunctio(display)
hello()