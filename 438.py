# 438. Find All Anagrams in a String
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans = []
        # start with initial window
        left = 0
        right = len(p)
        # get the value counts of p
        counts = {}
        for i,c in enumerate(p):
            counts[c] = counts.get(c, 0) + 1
        # get the value counts of initial window
        window = {}
        for i,c in enumerate(s[:len(p)]):
            window[c] = window.get(c, 0) + 1
        # slide window across all of s
        while right < len(s):
            # if counts are the same, we have anagram
            # note this is O(26), ie constant time
            if window == counts:
                ans.append(left)
            # add right pointer to window
            window[s[right]] = window.get(s[right], 0) + 1
            # remove left pointer from window
            window[s[left]] -= 1
            # if left pointer value is now 0, remove from dict
            if window[s[left]] == 0:
                del window[s[left]]
            left += 1
            right += 1
        # check after last iteration
        if window == counts:
            ans.append(left)
        return ans
