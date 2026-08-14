class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        ans = 0
        left = 0
        right = k
        curr = sum(nums[:k])
        counts = {}
        dups = set()
        for i,c in enumerate(nums[:k]):
            counts[c] = counts.get(c, 0) + 1
            if counts[c] > 1:
                dups.add(c)
        while right < len(nums):
            if not dups:
                ans = max(ans, curr)
            counts[nums[right]] = counts.get(nums[right], 0) + 1
            if counts[nums[right]] > 1:
                dups.add(nums[right])
            counts[nums[left]] -= 1
            if counts[nums[left]] == 1:
                dups.remove(nums[left])
            curr -= nums[left]
            curr += nums[right]
            left += 1
            right += 1
        if not dups:
            ans = max(ans, curr) 
        return ans
