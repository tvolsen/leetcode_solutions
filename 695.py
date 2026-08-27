# 695. Max Area of Island
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int: 
        m = len(grid)
        n = len(grid[0])
        ans = 0
        seen = set()
        def dfs(i,j):
            size = 1
            grid[i][j] = 0
            for x,y in [(1,0), (0,1), (-1,0), (0,-1)]:
                if 0 <= i+x < m and 0 <= j+y < n:
                    if grid[i+x][j+y] == 1:
                        size += dfs(i+x, j+y)
            return size
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    ans = max(ans, dfs(i,j))
        return ans
