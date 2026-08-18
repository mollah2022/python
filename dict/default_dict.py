from collections import defaultdict

data = defaultdict(list)

data["Python"].append("Sajib")
data["Python"].append("Rahim")

print(data)


students = [
    ("Python", "Sajib"),
    ("Python", "Rahim"),
    ("SQL", "Karim"),
    ("SQL", "Hasan")
]

from collections import defaultdict

result = defaultdict(list)

for subject, student in students:
    result[subject].append(student)

print(result)


from collections import Counter

numbers = [1, 2, 2, 3, 3, 3]

count = Counter(numbers)

print(count)

