# 55. Jump Game
class Solution:
    """
    the states in this problem are if we can reach the stair at index i
    """
    def canJump(self, nums: List[int]) -> bool:
        # the default value is False because we are changing which stairs we can reach as we iterate
        dp = [False] * len(nums)
        dp[0] = True
        for i in range(len(nums)):
            # if we cannot reach this stair, move on
            if dp[i] == False:
                continue
            for j in range(1, nums[i]+1):
                # if we arrive on the top step, exit early
                if i + j == len(nums):
                    return True
                # update that you can reach each step
                dp[i+j] = True
        # return if you can reach the final step or not
        return dp[-1]
            
