# 300. Longest Increasing Subsequence
class Solution:
    """
    the states in this problem are the len of the increasing subsequence ending at index i
    """
    def lengthOfLIS(self, nums: List[int]) -> int:
        # each subsequence of len 1 is increasing, so use 1 as default value
        dp = [1] * len(nums)
        # iterate through each index i
        for i in range(len(nums)):
            # iterate through each smaller index j < i
            for j in range(i):
                # if nums[i] > nums[j] it can be added to the subseq
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], dp[j] + 1)
        # return the len of the largest subseq
        return max(dp)
