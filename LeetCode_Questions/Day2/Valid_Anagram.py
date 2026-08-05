def isAnagram(s,t):
  if(len(s) != len(t)):
    return False

  count={}

  for i in s:
    if i in count:
      count[i] += 1
    else:
      count[i] =1 

  for i in t:
    if i not in count:
      return False
    count[i] -= 1
    if count[i]<0:
      return False
  return True

s = "nagpur"
t = "purnag"

result = isAnagram(s,t)
print(result)  # Output: True

# OR

def isAna(s,t):
  d1={}
  d2={}

  for i in s:
    if i in d1:
      d1[i] += 1
    else:
      d1[i] =1

  for i in t:
    if i in d2:
      d2[i] += 1
    else:
      d2[i] =1

  return d1 == d2

result1 = isAna(s,t)
print(result1)  # Output: True

p = "Dev"
q = "Nes"
result2 = isAna(p,q)
print(result2)  # Output: False
result3 = isAnagram(p,q)
print(result3)  # Output: False