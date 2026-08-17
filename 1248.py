# 1248. Count Number of Nice Subarrays
class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        prefix = []
        for i in range(len(nums)):
            odd = 0
            if nums[i] % 2 == 1:
                odd = 1
            if prefix:
                prefix.append(prefix[-1] + odd)
            else:
                prefix.append(odd)
        seen = {0:1}
        ans = 0
        for p in prefix:
            if p-k in seen:
                ans += seen[p-k]
            seen[p] = seen.get(p, 0) + 1
        return ans
