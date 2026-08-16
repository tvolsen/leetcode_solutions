# 2090. K Radius Subarray Averages
class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        avgs = [None for n in nums]
        curr = None
        for i in range(k, len(nums)-k):
            if not curr:
                curr = sum(nums[i-k:i+k+1])
            else:
                curr -= nums[i-k-1]
                curr += nums[i+k]
            avgs[i] = curr
        for i,a in enumerate(avgs):
            if a is None:
                avgs[i] = -1
            else:
                avgs[i] = avgs[i] // (2*k+1)
        return avgs
