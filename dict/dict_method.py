student = {
    "name": "Sajib",
    "age": 25,
    "city": "Dhaka"
}

print(student.keys())

for key in student.keys():
    print(key)

print(student.values())

print("----------------------------------")
print(student.items())


for key, value in student.items():
    print(key, value)




student = {
    "name": "Sajib",
    "age": 25
}

print(student.get("name", "Unknown"))
print(student.get("city", "Unknown"))


student.update({
    "city": "Dhaka",
    "age": 26
})

print(student)



student = {
    "name": "Sajib",
    "age": 25,
    "city": "Dhaka"
}

age = student.pop("age")

print(age)
print(student)


item = student.popitem()

print(item)
print(student)