fruits = ["apple","banana", "cherry", "date", "elderberry"]

# Accessing elements in the list
print(f"First fruit: {fruits[0]}")  # Accessing the first element
print(f"Last fruit: {fruits[-1]}")  # Accessing the last element

fruits[1] = "blueberry"  # Modifying the second element
print(f"Modified list: {fruits}")

# Adding elements to the list
fruits.append("fig")  # Adding an element at the end
print(f"List after appending: {fruits}")

fruits.insert(2, "coconut")  # Inserting an element at index 2
print(f"List after inserting: {fruits}")

# Removing elements from the list
fruits.remove("date")  # Removing an element by value
print(f"List after removing 'date': {fruits}")

popped_fruit = fruits.pop()  # Removing the last element and returning it
print(f"Popped fruit: {popped_fruit}")

print(f"Final list: {fruits}")

print(f"slicing the list from index 1 to 3: {fruits[1:4]}")  # Slicing the list)

print(f"Length of the list: {len(fruits)}")  # Getting the length of the list

for i in range(len(fruits)):
    print(f"Fruit at index {i}: {fruits[i]}")  # Iterating through the list using a for loop

for fruit in fruits:
    print(f"Fruit: {fruit}")  # Iterating through the list using a for-each loop

print( "apple" in fruits)  # Checking if an element exists in the list