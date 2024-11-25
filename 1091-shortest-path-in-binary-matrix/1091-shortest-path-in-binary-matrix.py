class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        maxRow = len(grid) - 1
        maxCol = len(grid[0]) - 1
        
        directions = [(1,1), (1,0), (0,1), (0,-1), (-1,0), (-1,1), (1,-1), (-1,-1)]
        
        if grid[0][0] != 0 or grid[maxRow][maxCol] != 0:
            return -1
        
        def getNeighbors(row, col):
            for rowDiff, colDiff in directions:
                newRow = row + rowDiff
                newCol = col + colDiff
                if not (0 <= newRow <= maxRow and 0 <= newCol <= maxCol):
                    continue
                if grid[newRow][newCol] != 0:
                    continue

                yield (newRow, newCol)
        
        queue = deque()
        queue.append((0,0,1))
        visited = {(0,0)}
        
        while queue:
            row, col,distance = queue.popleft()
            if (row, col) == (maxRow, maxCol):
                return distance
            for neighborR, neighborC, in getNeighbors(row, col):
                if (neighborR, neighborC) in visited:
                    continue
                visited.add((neighborR, neighborC))
                queue.append((neighborR, neighborC, distance+1))
            
        return -1
                