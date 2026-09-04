# 746. Min Cost Climbing Stairs
class Solution:
    """
    the state i in this problem represents the minimum number of steps to reach step i
    """
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # a dictionary storing all visisted states
        mem = {}
        def dp(i):
            # if you have seen this state before, return it
            if i in mem:
                return mem[i]
            # you can start on step 1 or 2
            if i < 2:
                return 0
            # choose to enter this step from 1 or 2 steps back
            mem[i] = min(dp(i-1) + cost[i-1], dp(i-2) + cost[i-2])
            # return the optimal value for step i
            return mem[i]
        # return the optimal value for the top step
        return dp(len(cost))



        # bottom up solution
        # dp = [cost[0], cost[1]]
        # for i in range(len(cost)):
        #     if i < 2:
        #         continue
        #     new = min(dp[i-1], dp[i-2]) + cost[i]
        #     dp.append(new)
        # return min(dp[-2:])
