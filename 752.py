# 752. Open the Lock
class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        from collections import deque
        def turn(i,j,vals):
            vals = list(vals)
            vals[i] = (vals[i] + j) % 10
            return tuple(vals)
        deadends = set([tuple([int(x) for x in y]) for y in deadends])
        target = tuple([int(x) for x in target])
        if (0,0,0,0) in deadends:
            return -1
        seen = set({})
        q = deque([((0,0,0,0), 0)])
        while q:
            vals, d = q.pop()
            if vals == target:
                return d
            for i in range(4):
                for j in [-1, 1]:
                    val = turn(i,j,vals)
                    if (val not in seen) and (val not in deadends):
                        q.appendleft((val, d+1))
                        seen.add(val)
        return -1
