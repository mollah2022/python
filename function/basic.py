def addition(a ,b):
    res = a + b
    return res

rec = addition(10,20)
print(rec)
rec = addition(20,30)
print(rec)

print(addition(2,3))


def calculate(a, b):
    addition = a + b
    subtraction = a - b
    multiplication = a * b

    return addition, subtraction, multiplication


result = calculate(10, 5)

print(result)

a, b, c = result

print(a)