# 881. Boats to Save People
class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # this problem is greedy because we want to pair the 
        # heaviest people with the lightest people to maximize
        # the capacity of each boat
        from collections import deque
        people.sort()
        # create a q for quick left and right popping
        q = deque(people)
        ans = 0
        while q:
            # if there is a single person left, they get the last boat
            if len(q) == 1:
                return ans + 1
            # if the lightest and heaviest people can both fit, send them off
            if q[0] + q[-1] <= limit:
                q.popleft()
                q.pop()
                ans += 1
            # otherwise send the heavist person off, since they cannot pair with anyone
            else:
                q.pop()
                ans += 1
        # return the number of boats needed
        return ans
            
