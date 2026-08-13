class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ans = 0
        left = 0
        seen = {}
        for right in range(len(s)):
            seen[s[right]] = seen.get(s[right], 0) + 1
            # this is O(26) = O(1) time
            hi = max(seen.values())
            total = sum(seen.values())
            while total > hi + k and left <= right:
                seen[s[left]] -= 1
                left += 1
                hi = max(seen.values())
                total = sum(seen.values())
            ans = max(ans, right-left+1)
        return ans
