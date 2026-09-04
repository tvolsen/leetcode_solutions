# 213. House Robber II
class Solution:
    """
    the states in this problem represent the maximum amount we have stolen
    up through house i
    """
    def rob(self, nums: List[int]) -> int:
        # if 2 or less houses, rob larger one
        if len(nums) <= 2:
            return max(nums)
        # helper function for each block described below
        def rob_block(block):
            # save your dp state history
            dp = [0] * len(block)
            # the most you can have at the first house is the value of the first house
            dp[0] = block[0]
            # the most you can have at the second house is the max of the first 2 homes
            dp[1] = max(block[0], block[1])
            # loop over all other homes
            for i in range(2, len(block)):
                # take the max over the 2 states we can arrive from
                dp[i] = max(
                    dp[i-1], # if we skip the curr house
                    dp[i-2] + block[i] # if we rob the curr house
                )
            return dp[-1]
        # since the houses are on a circle, consider two separate blocks
        # one with the first house and not the last house since they are adjacent
        # and one without the first house but include the last house
        start_first = rob_block(nums[:-1])
        start_second = rob_block(nums[1:])
        # return the max of these sub-blocks
        return max(start_first, start_second)
