# 875. Koko Eating Bananas
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        from math import ceil
        left = 1
        right = max(piles)
        while left <= right:
            mid = (left + right) // 2
            curr = sum([math.ceil(b/mid) for b in piles])
            if curr > h:
                left = mid + 1
            else:
                right = mid - 1
        return left
