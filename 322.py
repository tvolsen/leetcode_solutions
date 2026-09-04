# 322. Coin Change
class Solution:
    """
    the states in this problem represent the fewest number of coins required to make amount i
    """
    def coinChange(self, coins: List[int], amount: int) -> int:
        # we are taking minimums so default value is inf
        dp = [float(inf)] * (amount+1)
        # edge case
        dp[0] = 0
        # fill the dp array until i = amount + 1
        for i in range(len(dp)):
            # check all coin values
            for c in coins:
                # if we can make i with a single coin, break
                if i == c:
                    dp[c] = 1
                    break
                # look at previous states by subtracting the coin and taking minimum amount
                if i-c >= 0:
                    dp[i] = min(dp[i], dp[i-c] + 1)
        # if we cannot make the amount, return -1
        if dp[amount] == float(inf):
            return -1
        # return the min number of coins to make amount
        return dp[amount]
