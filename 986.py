# 986. Interval List Intersections
class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        A = sorted(firstList)
        B = sorted(secondList)
        a = 0
        b = 0
        ans = []
        while a < len(A) and b < len(B):
            starta, enda = A[a]
            startb, endb = B[b]
            if starta <= endb:
                if startb <= enda:
                    ans.append([max(starta, startb), min(enda, endb)])
            if enda <= endb:
                a += 1
            else:
                b += 1
        return ans
