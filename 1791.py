# 1791. Find Center of Star Graph
class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        g = {}
        for u,v in edges:
            if u not in g:
                g[u] = [v]
            else:
                return u
            if v not in g:
                g[v] = [u]
            else:
                return v
        print(g)
