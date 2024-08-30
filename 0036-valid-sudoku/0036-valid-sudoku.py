class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        ROWS = len(board)
        COLS = len(board[0])
        
        containsNumber = []
        for row in range(ROWS):
            containsNumber = []
            for col in range(COLS):
                if board[row][col].isdigit() and board[row][col] in containsNumber:
                    return False
                elif board[row][col].isdigit():
                    containsNumber.append(board[row][col])

        containsNumber = []
        for col in range(COLS):
            containsNumber = []
            for row in range(ROWS):
                if board[row][col].isdigit() and board[row][col] in containsNumber:
                    return False
                elif board[row][col].isdigit():
                    containsNumber.append(board[row][col])
            
        grid = []
        for row in [0,3,6]:
            for col in [0,3,6]:
                grid = []
                for x in range(row, row+3):
                    for y in range(col, col+3):
                        if board[x][y].isdigit() and board[x][y] in grid:
                            return False
                        elif board[x][y].isdigit():
                            grid.append(board[x][y])
        return True
            