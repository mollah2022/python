numbers = [10,2,13,1,5,8,93,6,4,7]

sorted_numbers = sorted(numbers)  # Returns a new sorted list
numbers.sort()  # Sorts the original list in place

print("Original list:", numbers)
print("Sorted list (using sorted()):", sorted_numbers)


names = ["rakib", "sajib", "ahmed", "tuhin", "shuvo"]
sorted_names = sorted(names, key=len)  # Returns a new sorted list based on length of names
names.sort(key=len)  # Sorts the original list in place based on length of names

print("Original list of names:", names)
print("Sorted list of names (using sorted()):", sorted_names)

""" sort vs sorted diff in python
1. sorted() function returns a new sorted list from the elements of any iterable (like list, tuple, dictionary, etc.) and does not modify the original iterable. It can be used with any iterable and returns a new list.
2. sort() method is a method of list objects and sorts the list in place, modifying the original list. It can only be used with lists and does not return a new list. It returns None.
3. sorted() can take any iterable as input
4. sort() can only be used with lists
5. sorted() can be used with the key parameter to specify a function to be called on each element prior to making comparisons, while sort() can also take a key parameter for the same purpose
6. sorted() can take a reverse parameter to sort in descending order, while sort() can also take a reverse parameter for the same purpose
7. sorted() can be used in expressions and can be assigned to a variable, while sort() cannot be used in expressions and does not return a value (returns None)
8. sorted() can be used with any iterable, while sort() can only be used with lists
9. sorted() can be used to sort any iterable, while sort() can only be used to sort lists
10. sorted() can be used to sort any iterable
""" 


fruits = ["apple", "banana", "cherry", "date", "elderberry"]

sorted_fruits = sorted(fruits, reverse=True)  # Returns a new sorted list in descending order
fruits.sort(reverse=True)  # Sorts the original list in place in descending order

print("Original list of fruits:", fruits)
print("Sorted list of fruits (using sorted()):", sorted_fruits)