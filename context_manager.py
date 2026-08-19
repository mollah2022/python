numbers = [1,3,4,5,6,7]

numbers_mul = [ number * number for number in numbers]
numbers_mult = ( number * number for number in numbers)

print(numbers_mul)
print(numbers_mult)

for number_mult in numbers_mult:
    print(number_mult)



def calculator():
    while True:
        number = yield
        print(number * 2)


gen = calculator()

next(gen)

gen.send(10)
gen.send(20)
gen.send(30)