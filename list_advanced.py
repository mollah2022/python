numbers = [1,2,3,4,5,6,7,8,9,10]

# Unpacking the list into variables
a, b, c, *d = numbers

print(a)
print(b)
print(c)
print(d)

n, *m, o = numbers

print("======================================")


print(n)
print(m)
print(o)

print("======================================")

p, *_, q = numbers
print(p)
print(q)

print("--------------------------------------")

""" enumerate() function is used to iterate over a list and get the index and value of each element in the list. """


fruits = ["apple", "banana", "cherry", "mango", "elderberry"]

for index, fruit in enumerate(fruits, start = 1):
    print(f"Index: {index}, Fruit: {fruit}")


print("----------------------------------------")

for index, fruit in enumerate(fruits, start = 1):
    if fruit == "mango":
        fruits[index - 1] = "Orange"  # Replace "mango" with "Orange"
        break  # Exit the loop after replacing

print(f"Updated list: {fruits}")