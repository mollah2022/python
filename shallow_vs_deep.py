""" 
Python creates a shallow copy.
Very simple meaning:
The outer list is copied, but nested objects may still be shared.
"""

a = [[1, 2], [3, 4]]

b = a.copy()

b[0].append(100)

print(a)
print(b)

""" 
If you have nested lists and want a completely separate copy, you can use:
"""
import copy

a = [[1, 2], [3, 4]]

b = copy.deepcopy(a)

b[0].append(100)

print(a)
print(b)

"""
Shallow copy : 
             Outer list → copied
             Inner lists → shared

Deep copy :
          Outer list → copied
          Inner lists → copied
          Everything nested → copied
"""