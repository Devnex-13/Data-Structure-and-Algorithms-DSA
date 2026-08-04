def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        l = set()

        for num in nums:
            if(num in l):
                return True
                break
            else:
               l.add(num)
        return False

nums = [1, 2, 3, 1]

result = containsDuplicate(None, nums)
print(result)  # Output: True 