# 841. Keys and Rooms
class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        g = {}
        for i in range(len(rooms)):
            g[i] = rooms[i]
        seen = set()
        def dfs(v):
            seen.add(v)
            if len(seen) == len(rooms):
                return True
            for u in g[v]:
                if u in seen:
                    continue
                if dfs(u):
                    return True
            return False
        return dfs(0)
