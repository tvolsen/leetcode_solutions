# 70. Climbing Stairs
class Solution:
    def climbStairs(self, n: int) -> int:
        # the previously observed states are stored here
        dp = [0] * (n+1)
        # there is only 1 way to reach each step 0 and step 1
        dp[0] = 1
        dp[1] = 1
        # loop over stairs 2 to n
        for i in range(2, n+1):
            # you can reach step i by taking 2 steps from step i-2
            # or by taking 1 step from step i - 1, thus add them
            dp[i] = dp[i-1] + dp[i-2]
        # return the total number of ways to reach step n
        return dp[n]
