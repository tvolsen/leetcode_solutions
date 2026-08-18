# 202. Happy Number
class Solution:
    def isHappy(self, n: int) -> bool:
        n = str(n)
        seen = []
        curr = 0
        while curr != 1:
            curr = 0
            for i,c in enumerate(n):
                curr += int(c)**2
            seen.append(curr)
            n = str(curr)
            if len(seen) != len(set(seen)):
                return False
        return True
