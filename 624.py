 624. Maximum Distance in Arrays
class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        lo = arrays[0][0]
        hi = arrays[0][-1]
        ans = 0
        for i in range(1, len(arrays)):
            curr_lo = arrays[i][0]
            curr_hi = arrays[i][-1]
            diff1 = abs(lo - curr_hi)
            diff2 = abs(hi - curr_lo)
            ans = max(ans, diff1, diff2)
            lo = min(curr_lo, lo)
            hi = max(curr_hi, hi)
        return ans
