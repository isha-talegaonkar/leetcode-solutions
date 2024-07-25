class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        numRows = len(image)
        numCols = len(image[0])
        
        originalColor = image[sr][sc]
        if originalColor == color:
            return image
        
        def dfs(row, col):
            if image[row][col] == originalColor:
                image[row][col] = color
                
                if row >= 1:
                    dfs(row-1, col)
                if row+1 < numRows:
                    dfs(row+1, col)
                if col >= 1:
                    dfs(row, col-1)
                if col+1 < numCols:
                    dfs(row, col+1)
        
        dfs(sr, sc)
        return image
        
        