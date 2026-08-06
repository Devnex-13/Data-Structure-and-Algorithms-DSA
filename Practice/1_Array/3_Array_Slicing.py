from array import *

val = array('i', [1,2,3,4,5,6])

# name[start index: end index: step]

print(val[1:5]) # Output: array('i', [2, 3, 4, 5])

print(val[1:5:2]) # Output: array('i', [2, 4])

print(val[:5]) # Output: array('i', [1, 2, 3, 4, 5])

print(val[1:]) # Output: array('i', [2, 3, 4, 5, 6])

print(val[:]) # Output: array('i', [1, 2, 3, 4, 5, 6])

print(val[::2]) # Output: array('i', [1, 3, 5])

# To Reverse The Array:
print(val[::-1]) # Output: array('i', [6, 5, 4, 3, 2, 1])

print(val[-5:-1]) # Output: array('i', [2, 3, 4, 5])