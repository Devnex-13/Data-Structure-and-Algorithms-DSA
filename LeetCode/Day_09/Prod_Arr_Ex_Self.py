from math import *

def productExceptSelf(nums):
  answer = [1]*len(nums)
  right = [1]*len(nums)

  for r in range(len(nums)):
    if r>0:
      answer[r] = answer[r-1]*nums[r-1]

  for r in range(len(nums)-1,-1,-1):
    if r<len(nums)-1:
      right[r] = right[r+1]*nums[r+1]

  for r in range(len(answer)):
    answer[r] *= right[r]

  return answer

arr = [1,2,3,4,5]
print(productExceptSelf(arr))