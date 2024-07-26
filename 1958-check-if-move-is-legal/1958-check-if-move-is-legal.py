class Solution:
    def checkMove(self, board: List[List[str]], rMove: int, cMove: int, color: str) -> bool:
        numRows = len(board)
        numCols = len(board[0])
        
        def dfs(row, col, dx, dy, distance, color):
            if board[row][col] == color and distance > 1:
                return True
            if board[row][col] == color and distance == 1:
                return False

            nextX = row + dx
            nextY = col + dy
            if 0 <= nextX < numRows and 0 <= nextY < numCols and board[nextX][nextY] != '.':
                if dfs(nextX, nextY, dx, dy, distance + 1, color):
                    return True
            return False
        directions = [[0, -1], [-1, -1], [-1, 0], [-1, 1],[0, 1], [1, 1],[1, 0], [1, -1]]
        for dx, dy in directions:
            if dfs(rMove, cMove, dx, dy, 0, color):
                return True

        return False