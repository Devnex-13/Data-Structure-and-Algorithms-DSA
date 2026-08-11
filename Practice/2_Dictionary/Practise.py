# def lengthOfLongestSubstring(s):
#         """
#         :type s: str
#         :rtype: int
#         """

#         l=0
#         n=len(s)
#         Hashmap = {}
#         max_len = 0

#         for r in range(l,n):
#             if s[r] in Hashmap:
#                 l = Hashmap[s[r]]+1
#             Hashmap[s[r]]=r
#             max_len = max(max_len, r - l + 1)
#         return max_len  

# s = 'ccbbcc'
# print(lengthOfLongestSubstring(s))

# dict = {
#     "dec":12,
#     "pote":10
# }

# print(max(dict.values()))

def checkInclusion(s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """
        l=0
        freq={}

        for i in s1:
            if i in freq:
                freq[i] +=1
            else:
                freq[i] = 1
        print(freq)
        
        for r in s2:
            if r in freq and freq[r] > 0:
                freq[i] -= 1
            else:
                print(s2.index(r))
                l = s2.index(r)+1
        print(freq)

        if(not any(freq.values())):
             return True
        else:
             return False

s1 = "ab"
s2 = "hwiwnbajsf"

print(checkInclusion(s1,s2))