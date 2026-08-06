def ReverseStr(s):
  l=0
  r= len(s)-1
  while l < r:
    temp = s[l]
    s[l] = s[r]
    s[r] = temp

    l+=1
    r-=1
  return s

s1 = ["D","e","v","a","n","s","h","u"]

print(ReverseStr(s1))