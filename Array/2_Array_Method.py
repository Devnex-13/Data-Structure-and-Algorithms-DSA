import array as arr 
# OR
# from array import * (No need to use arr.array() in this case) 

val = arr.array('i',[1,2,3,4,5,6])
# val = array('i',[1,2,3,4,5,6]) (if you use from array import *)

print(val)

for i in val:
  print(i, end=" ")

# to Find Type code:
print("\n")
print(val.typecode)

# to reverse Array
val.reverse()
print(val) # Output: array('i', [6, 5, 4, 3, 2, 1])

# insert an element in array
val.insert(2, 0) # insert 0 at index 2
print(val) # Output: array('i', [6, 5, 0, 4, 3, 2, 1])

# Add element At the end of array
val.append(7) # append 7 at the end of array
print(val) # Output: array('i', [6, 5, 0, 4, 3, 2, 1, 7])

# to Overwrite an element in array
val [2] = 10 # overwrite element at index 2 with 10 
print(val) # Output: array('i', [6, 5, 10, 4, 3, 2, 1, 7])

# to copy an array
val2 = arr.array(val.typecode, val)
print(val2) # Output: array('i', [6, 5, 10, 4, 3, 2, 1, 7])

# to remove an element from array
val.remove(10) # remove 10 from array
print(val) # Output: array('i', [6, 5, 4, 3, 2, 1, 7])

# To remove an element from array at a specific index
val.pop(2) # remove element at index 2
print(val) # Output: array('i', [6, 5, 3, 2, 1, 7])

# To find the index of an element in array
print(val.index(3)) # Output: 2

# To find the length of an array
print(len(val)) # Output: 6

# To find the maximum and minimum element in an array
print(max(val)) # Output: 7
print(min(val)) # Output: 1

# To find the sum of all elements in an array
print(sum(val)) # Output: 24

# To Delete an array
del val
