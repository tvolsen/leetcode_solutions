# 735. Asteroid Collision
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        i = 0
        while i < len(asteroids):
            a = asteroids[i]
            if not stack:
                stack.append(a)
                i += 1
            else:
                if stack[-1] * a > 0 or stack[-1] < 0:
                    stack.append(a)
                    i += 1
                else:
                    if abs(stack[-1]) > abs(a):
                        i += 1
                    elif abs(stack[-1]) < abs(a):
                        stack.pop()
                    else:
                        stack.pop()
                        i += 1
        return stack 
