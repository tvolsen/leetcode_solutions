# 1323. Maximum 69 Number
class Solution:
    def maximum69Number (self, num: int) -> int:
        s = str(num)
        ans = ''
        swapped = False
        for c in s:
            if c == '6' and swapped == False:
                ans += '9'
                swapped = True
            else:
                ans += c
        return int(ans)
