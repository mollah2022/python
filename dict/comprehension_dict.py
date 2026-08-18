numbers = [1, 2, 3, 4, 5, 6]

even_numbers = {
    number: number * number
    for number in numbers
    if number % 2 == 0
}

print(even_numbers)



keys = ["name", "age", "city"]
values = ["Sajib", 25, "Dhaka"]

student = dict(zip(keys, values))

print(student)