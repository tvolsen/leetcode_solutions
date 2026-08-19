# 71. Simplify Path
class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        path = path.split('/')
        for c in path:
            if not c:
                continue
            elif c == '..':
                if stack:
                    stack.pop()
            elif c == '.':
                continue
            else:
                stack.append(c)
        return '/' + '/'.join(stack)
