student = {
    "name":"Sajib Ahmed",
    "age":25,
    "city":"Dhaka"
}

print(student)

student["name"] = "Tamim Iqbal"

print(student)

student["gender"] = "Male"

print(student)


data = {
    "name": "Sajib",
    "age": 25,
    "skills": ["Python", "SQL", "PySpark"],
    "address": {
        "city": "Dhaka",
        "country": "Bangladesh"
    }
}

print(data.keys())
print(data.values())

data["address"]["city"] = "London"

print(data)


person = {
    "name": "Sajib",
    "age": 25,
    "job": "Engineer"
}

print(person["name"])

person["age"] = 26

person["city"] = "Dhaka"

del person["job"]

print(person)