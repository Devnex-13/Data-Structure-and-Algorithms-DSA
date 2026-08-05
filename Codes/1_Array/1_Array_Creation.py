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