def lengthOfLongestUniqueString(s):

  l = 0
  n = len(s)
  Hashmap={}
  max_len = 0

  for r in range(0,n):
      if s[r] in Hashmap:
         l = max(l,Hashmap[s[r]]+1)
      Hashmap[s[r]] = r
      max_len = max(max_len, r-l+1)

  return max_len

s = "cchdhshdahd"
print(lengthOfLongestUniqueString(s))