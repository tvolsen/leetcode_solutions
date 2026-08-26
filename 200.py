# 200. Number of Islands
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # find the neighbors of each spot in grid
        def neighbors(i, j, grid):
            # start with an empty list
            neighs = []
            # check directly north, south, east and west
            for x,y in [(1,0), (0,1), (-1,0), (0,-1)]:
                # make sure the new points are in the bounds of grid
                if 0 <= i+x < len(grid) and 0 <= j+y < len(grid[0]):
                    # only add the edge if the neighbor is land
                    if grid[i+x][j+y] == "1":
                        neighs.append((i+x, j+y))
            # return the neighbor set
            return neighs
        # track what has been seen to avoid infinite loops in graph cycles
        seen = set()
        # standard DFS
        def dfs(i, j):
            neighs = neighbors(i, j, grid)
            for neigh in neighs:
                a, b = neigh
                # only explore unseen nodes
                if (a, b) not in seen:
                    seen.add((a, b))
                    dfs(a, b)
        # 0 islands to start
        ans = 0
        # loop over entire grid
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                # skip water locations
                if grid[i][j] == "0":
                    continue
                # new island found, explore it and update ans
                if (i, j) not in seen:
                    ans += 1
                    dfs(i, j)
        return ans

        
