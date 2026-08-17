numbers = [1,2,3,4,5,6,7,8]

numbers_copy = numbers

numbers_copy[0] = 100

print("Original list:", numbers)
print("Copied list:", numbers_copy)
print( numbers is numbers_copy)  # True, both variables point to the same list object

print("--------------------------------------")

num1 = [1,3,5,7,9]
num2 = num1.copy()  # Creates a shallow copy of the list

num2.append(11)

print("Original list:", num1)
print("Copied list:", num2)
print(num1 is num2)  # False, they are different list objects

print("--------------------------------------")

list1 = [2,4,6,8,10]
list2 = list(list1)  # Creates a shallow copy of the list

list2.remove(4)
print("Original list:", list1)
print("Copied list:", list2)
print(list1 is list2)  # False, they are different list objects


print("--------------------------------------")

a = [1,2,3,4,5]
b = [1,2,3,4,5]

print(a == b)
print( a is b)