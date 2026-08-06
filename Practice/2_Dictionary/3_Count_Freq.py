nums = [1,2,3,1]

def countFreq(nums):
    freq= {}
    for num in nums:
        if num in freq:
            freq[num] +=1
        else:
            freq[num] = 1
    return freq

result = countFreq(nums)
print(result)