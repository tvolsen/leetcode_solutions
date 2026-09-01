# 216. Combination Sum III
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []
        def bt(curr, hi):
            if len(curr) == k and sum(curr) == n:
                ans.append(curr[:])
                return
            for j in range(hi+1, 10):
                if sum(curr) + j <= n:
                    curr.append(j)
                    bt(curr[:], j)
                    curr.pop()
        bt([], 0)
        return ans
