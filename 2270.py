# 2270. Number of Ways to Split Array
class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        total = sum(nums)
        prefix = [nums[0]]
        for i in range(1, len(nums)):
            prefix.append(prefix[-1] + nums[i])
        ans = 0   
        for i in range(len(prefix)-1):
            p = prefix[i]
            if p >= total - p:
                ans += 1
        return ans
