# 1700. Number of Students Unable to Eat Lunch
class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        from collections import deque
        sandwiches = sandwiches[::-1]
        q = deque(students)
        counter = 0
        while q:
            if not sandwiches:
                return len(q)
            if sandwiches[-1] == q[0]:
                sandwiches.pop()
                q.popleft()
                counter = 0
            else:
                q.append(q.popleft())
                counter += 1
                if counter == len(q):
                    return len(q)
        return len(q)
