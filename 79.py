# 79. Word Search
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        def bt(i, j, curr, seen):
            if curr == word:
                return True
            if len(curr) > len(word):
                return False
            for x,y in [(1,0),(0,1),(-1,0),(0,-1)]:
                if 0 <= i+x < m and 0 <= j+y < n:
                    if (i+x, j+y) not in seen and board[i+x][j+y] == word[len(curr)]:
                        seen.add((i+x, j+y))
                        curr += board[i+x][j+y]
                        if bt(i+x, j+y, curr, seen):
                            return True
                        curr = curr[:-1]
                        seen.remove((i+x, j+y))
            return False
        m = len(board)
        n = len(board[0])
        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    if bt(i, j, word[0], set({(i,j)})):
                        return True
        return False
    
