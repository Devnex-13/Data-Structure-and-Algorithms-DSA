def MaxAverage(nums, k):
    n = len(nums)
    window_sum = sum(nums[0:k])
    max_average = window_sum/float(k)
        
    for r in range(k,n):
        window_sum += nums[r] - nums[r-k]
        average = window_sum/float(k)
        max_average = max(max_average, average)
    return max_average

nums = [1,12,-5,-6,50,3]
k =4
print(MaxAverage(nums, k))