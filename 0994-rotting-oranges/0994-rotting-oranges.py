from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        freshOranges = 0
        
        numRows = len(grid)
        numCols = len(grid[0])
        
        for r in range(numRows):
            for c in range(numCols):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    freshOranges += 1

        queue.append((-1, -1))
        
        minutes = -1
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        
        while queue:
            row, col = queue.popleft()
            if row == -1:
                minutes += 1
                if queue:
                    queue.append((-1, -1))
            else:
                for d in directions:
                    n_row, n_col = row + d[0], col + d[1]
                    if numRows > n_row >= 0 and numCols > n_col >= 0:
                        if grid[n_row][n_col] == 1:
                            grid[n_row][n_col] = 2
                            freshOranges -= 1
                            queue.append((n_row, n_col))
        return minutes if freshOranges == 0 else -1