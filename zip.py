name = ["Sajib", "Ahmed", "John", "Doe"]
age = [25, 30, 35, 40]
designation = ["Engineer", "Manager", "Director", "CEO"]

zipped_list = list(zip(name, age, designation))

print(f"Zipped list: {zipped_list}")


for N, A, D in zip(name, age, designation):
    print(N, " ",A, " ", D)


for index, (N, A, D) in enumerate(zip(name, age, designation), start=1):
    print(index, ":", N, " ", A, " ", D)

print("------------------------------------")

list_to_dict = dict(zip(name, zip(age, designation)))

print(list_to_dict)