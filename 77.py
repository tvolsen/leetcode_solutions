# 77. Combinations
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []
        def bt(i, curr):
            if len(curr) == k:
                ans.append(curr[:])
            for hi in range(i, n+1):
                curr.append(hi)
                bt(hi+1, curr)
                curr.pop()
        bt(1, [])
        return ans
