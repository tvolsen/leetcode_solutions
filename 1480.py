# 1480. Running Sum of 1d Array
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        prefix = []
        for i,n in enumerate(nums):
            if i == 0:
                prefix.append(nums[0])
            else:
                prefix.append(prefix[-1] + n)
        return prefix
