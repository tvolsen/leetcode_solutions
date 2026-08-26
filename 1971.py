# 1971. Find if Path Exists in Graph
class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        from collections import deque
        # create an empty graph
        g = {}
        # add all vertices to the graph
        for i in range(n):
            g[i] = []
        # add the edges to the graph
        for u,v in edges:
            g[u].append(v)
            g[v].append(u)
        # I usually prefer BFS for most problems, since I find recursion tricky
        q = deque([source])
        # we have cycles in general graphs, so we need a seen set to avoid infinite loops
        seen = set([source])
        # typical BFS
        while q:
            v = q.popleft()
            # if we found a path, return True
            if v == destination:
                return True
            # add the neighbors to the q
            for neigh in g[v]:
                # only add unseen neighbors
                if neigh not in seen:
                    q.append(neigh)
                    # update seen here, to greatly reduce possible q size
                    seen.add(neigh)
        # if destination is not found, return False
        return False
        
