# 268. Missing Number
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        missing = set([x for x in range(len(nums)+1)])
        for n in nums:
            missing.remove(n)
        return missing.pop()
        ''' 
        alternate answer with only math
        n = len(nums)
        s = sum(nums)
        return ((n**2 + n) // 2) - s
        '''
