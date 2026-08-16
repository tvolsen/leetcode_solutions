# 1456. Maximum Number of Vowels in a Substring of Given Length
class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = set('aeiou')
        curr = 0
        for i in range(k):
            if s[i] in vowels:
                curr += 1
        ans = curr
        i = k
        while i < len(s):
            if s[i-k] in vowels:
                curr -= 1
            if s[i] in vowels:
                curr += 1
            ans = max(ans, curr)
            i += 1
        return ans
