from numpy import *

val = array([1,2,3,4,5,6])

for x in val:
  print(x, end=" ")

print("\n")

# In Python, We can Create Heterogeneous Array using numpy.array() method. 
# In this case, We have to use dtype=object parameter in array() method.

arr = array([1, 2.5, 'Python', True], dtype=object)

for x in arr:
  print(x, end=" ")