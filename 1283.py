# 1283. Find the Smallest Divisor Given a Threshold
class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        from math import ceil
        left = 1
        right = sum(nums) + 1
        while left <= right:
            mid = (left + right) // 2
            curr = sum([math.ceil(x/mid) for x in nums])
            if curr > threshold:
                left = mid + 1
            else:
                right = mid - 1
        return left
