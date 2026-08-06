def MergerAlternate(word1, word2):
  l=0
  r=0
  s=""
  n = min(len(word1),len(word2))

  while r<n:
    s+=word1[l]
    s+=word2[r]
    l+=1
    r+=1
  if(len(word1)<len(word2)):
    s+=word2[r:]
  else:
    s+=word1[l:]
  return s

word1 = "abc"
word2 = "pqr"

print(MergerAlternate(word1, word2)) # Output: apbqcr

w1 = "dev"
w2 = "pote"
print(MergerAlternate(w1,w2)) # Output: dpeovte