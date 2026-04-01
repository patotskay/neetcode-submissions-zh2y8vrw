class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        for row in board:
            nums = [b for b in row if b != "."]
            if len(nums) != len(set(nums)):
                return False
        
        for col in range(9):
            nums = [board[row][col] for row in range(9) if board[row][col] != "."]
            if len(nums) != len(set(nums)):
                return False

        for row in range(0, 9, 3):
            for col in range(0,9, 3):
                nums = []
                for r in range(row, row + 3):
                    for c in range(col, col + 3):
                        if board[r][c] !=  ".":
                            nums.append(board[r][c])
                if len(nums) != len(set(nums)):
                    return False
        
        return True
