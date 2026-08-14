# 1004. Max Consecutive Ones III
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        # ans, left pointer and num flips
        ans = 0
        left = 0
        flips = 0
        # iterate over entire array
        for right in range(len(nums)):
            # add right pointer to window
            if nums[right] == 0:
                flips += 1
            # while window invalid, remove left and iterate
            while flips > k:
                if nums[left] == 0:
                    flips -= 1
                left += 1
            # update ans by len of now valid window
            ans = max(ans, right - left + 1)
        return ans
