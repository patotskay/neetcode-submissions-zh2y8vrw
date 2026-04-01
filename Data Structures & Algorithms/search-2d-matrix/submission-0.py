class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n = len(matrix[0]) - 1
        for row in matrix:
            l = 0
            r = n
            while r >= l:
                m = (r + l)//2
                if target > row[m]:
                    l = m + 1
                elif target < row[m]:
                    r = m - 1
                elif target == row[m]:
                    return True
        return False
