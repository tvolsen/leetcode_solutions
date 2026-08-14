class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # follow template for initial window
        left = 0
        right = k
        curr = sum(nums[:right])
        ans = curr
        # iterate until right reaches end of nums
        while right < len(nums):
            # add right pointer to window
            curr += nums[right]
            # remove left pointer from window
            curr -= nums[left]
            # shift window by 1
            left += 1
            right += 1
            # update ans
            ans = max(ans, curr)
        return ans / k
