from array import *

val = array('i', [])

n = int(input("Enter The total number of element in Array: "))

for i in range(n):
  val.append(int(input("Enter The element: ")))

for i in val:
  print(i, end=" ")