class Solution:
    def checkMove(self, board: List[List[str]], rMove: int, cMove: int, color: str) -> bool:
        numRows = len(board)
        numCols = len(board[0])
        
        directions = [[0,1],[1,0],[0,-1], [-1,0],[-1,1],[1,-1],[-1,-1],[1,1]]
        
        def isLegal(row, col, d):
            row, col = row + d[0], col + d[1]
            distance = 1
            while row >= 0 and row < numRows and col >= 0 and col < numCols:
                distance += 1
                if board[row][col] == ".":
                    return False
                if board[row][col] == color:
                    return distance >= 3
                
                row, col = row + d[0], col + d[1]
            return False
        
        for d in directions:
            if isLegal(rMove, cMove, d):
                return True