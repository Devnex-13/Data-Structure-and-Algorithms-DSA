def solve(nums, target):
  Hashmap = {}

  for index, value in enumerate(nums):
    t = target - value
    if t in Hashmap:
      return [Hashmap[t], index]
    else:
      Hashmap[t] = index

nums = [2, 7, 11, 15]
nums1 = [1,2,1,2]
target = 9
target1 = 2

result = solve(nums, target)
print(result)  # Output: [0, 1]
result1 = solve(nums1, target1)
print(result1)  # Output: [0, 2]