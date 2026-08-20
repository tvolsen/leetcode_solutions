# 74. Search a 2D Matrix
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        # find row index
        top = 0
        bot = len(matrix) - 1
        while top <= bot:
            mid = (top + bot) // 2
            if matrix[mid][0] == target:
                return True
            elif target < matrix[mid][0]:
                bot = mid - 1
            else:
                top = mid + 1
        i = bot

        # find col index
        left = 0
        right = len(matrix[0]) - 1
        while left <= right:
            mid = (left + right) // 2
            if matrix[i][mid] == target:
                return True
            elif target < matrix[i][mid]:
                right = mid - 1
            else:
                left = mid + 1
        j = right

        return False
