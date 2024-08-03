class Solution:
    def dfs(self, row, col, grid):
        if(row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]) or grid[row][col] != "1"):
            return 
        
        grid[row][col] = "0"
        
        self.dfs(row+1, col, grid)
        self.dfs(row-1, col, grid)
        self.dfs(row, col+1, grid)
        self.dfs(row, col-1, grid)
        
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS = len(grid)
        COLS = len(grid[0])
        
        numberOfIslands = 0
           
        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == "1":
                    self.dfs(row, col, grid)
                    numberOfIslands += 1
        return numberOfIslands
                    

    

        
            