# 561. Array Partition
class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        # this solution is straight forward, but knowing to use greedy is the challenge
        # we can use greedy here because we are taking the min between all pairs
        # that is, we want to group as many small numbers together as possible
        # so that the min choose a smaller number over another small number
        # rather than choosing a small number over a large number
        
        # sort the nums
        nums.sort()
        # running sum
        ans = 0
        while nums:
            # pop out your pair
            a = nums.pop()
            b = nums.pop()
            # update ans with the min
            ans += min(a,b)
        return ans
