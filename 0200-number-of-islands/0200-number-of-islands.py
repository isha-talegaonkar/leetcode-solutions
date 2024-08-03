class Solution:
    def isValid(self, grid, r, c):
        if len(grid) > r >= 0 and len(grid[0]) > c >= 0:
            return True

    def dfs(self, grid, r, c):
        if self.isValid(grid, r, c) and grid[r][c] == "1":
            grid[r][c] = "0"
        else:
            return
        
        self.dfs(grid, r-1, c)
        self.dfs(grid, r+1, c)
        self.dfs(grid, r, c-1)
        self.dfs(grid, r, c+1)
        
    def numIslands(self, grid: List[List[str]]) -> int:

        if not grid:
            return 0
        
        numIslands = 0
        numRows = len(grid)
        numCols = len(grid[0])
            
        for r in range(numRows):
            for c in range(numCols):
                if grid[r][c] == "1":
                    self.dfs(grid, r, c)
                    numIslands += 1
        return numIslands
    

        
            