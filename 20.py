# 20. Valid Parentheses
class Solution:
    def isValid(self, s: str) -> bool:
        # define the stack
        stack = []
        for i,c in enumerate(s):
            # if you open a brace, you must add it to stack
            if c in ['(', '{', '[']:
                stack.append(c)
            # if you close ), check if the last element is (
            # if so, remove it and do not append new )
            elif c == ')':
                if stack and stack[-1] == '(':
                    stack.pop()
                else:
                    stack.append(c)
            # repeated logic for {}
            elif c == '}':
                if stack and stack[-1] == '{':
                    stack.pop()
                else:
                    stack.append(c)
            # repeated logic for []
            elif c == ']':
                if stack and stack[-1] == '[':
                    stack.pop()
                else:
                    stack.append(c)
        # if the stack has any elements, it is not valid
        if stack:
            return False
        # otherwise, it is valid
        else:
            return True
