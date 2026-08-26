# 994. Rotting Oranges
from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque([])
        m = len(grid)
        n = len(grid[0])
        count = 0
        seen = {}
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    count += 1
                if grid[i][j] == 2:
                    q.append((i, j, 0))
        if count == 0:
            return 0
        while q:
            i,j,d = q.popleft()
            for x,y in [(1,0), (0,1), (-1,0), (0,-1)]:
                if 0 <= i+x < m and 0 <= j+y < n:
                    if grid[i+x][j+y] == 1:
                        grid[i+x][j+y] = 2
                        count -= 1
                        if count == 0:
                            return d+1
                        q.append((i+x, j+y, d+1))
        return -1
