# 649. Dota2 Senate
class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        from collections import deque
        r = deque([])
        d = deque([])
        n = len(senate)
        for i,v in enumerate(senate):
            if v == 'R':
                r.append(i)
            else:
                d.append(i)
        while r and d:
            if r[0] < d[0]:
                r.append(r.popleft() + n)
                d.popleft()
            else:
                d.append(d.popleft() + n)
                r.popleft()
        if r:
            return 'Radiant'
        else:
            return 'Dire'
