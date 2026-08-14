# 209. Minimum Size Subarray Sum
class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # ans, left pointer and current sum 
        ans = float('inf')
        left = 0
        curr = 0
        # iterate over entire array
        for right in range(len(nums)):
            # add right element to window
            curr += nums[right]
            # while window IS valid
            while curr >= target:
                # update ans
                ans = min(ans, right - left + 1)
                # remove left element and iterate left
                curr -= nums[left]
                left += 1
        # no valid windows, return 0
        if ans == float('inf'):
            return 0
        return ans
