def rotate(nums, k):
  n = len(nums)

  temp= [0]*n

  for i in range(n):
    temp[(i+k)%n] = nums[i]

  for i in range(n):
    nums[i] = temp[i]

  return nums

nums = [1,2,3,4,5,6,7]
k = 3
result = rotate(nums, k)
print(result)  # Output: [5, 6, 7, 1, 2, 3, 4]