def search(nums, target):
  """
  :type nums: List[int]
  :type target: int
  :rtype: int
  """
  l = 0
  r = len(nums)-1
  while l<=r:
      mid = l+(r-l)//2
      if(target == nums[mid]):
          return mid
      
      elif(target < nums[mid]):
          r = mid - 1
      else:
          l = mid + 1       
  return -1

a = [1,4,6,7,8,9]
t = 9
result = search(a,t)
print(result)