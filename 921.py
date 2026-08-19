# 921. Minimum Add to Make Parentheses Valid
class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        for p in s:
            if stack and stack[-1] == '(' and p == ')':
                stack.pop()
            else:
                stack.append(p)
        return len(stack)
