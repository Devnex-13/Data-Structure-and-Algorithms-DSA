import re


def isPalindrome(s):
  s = re.sub(r'[a-zA-Z0-9]', '', s)
  s = s.lower()
  return s == s[::-1]

# OR

def isPalid(s):
  s = re.sub(r'[a-zA-Z0-9]', '', s)
  s = s.lower()
  l = 0
  r = len(s)

  while l < r:
    if s[l] == s[r]:
      l+=1
      r-=1
    else:
      return False
  return True

s1 = "A man, a plan, a canal: Panama"
s2 = "Madam"

print(isPalindrome(s1))
print(isPalindrome(s2))
print(isPalid(s1))
print(isPalid(s2))