class Solution:        
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        def dfs(node):
            if node in visited:
                return False
            if adjacencyList[node] == []:
                return True
            visited.add(node)

            for prereq in adjacencyList[node]:
                if not dfs(prereq): return False
            
            visited.remove(node)
            adjacencyList[node] = []
            return True
            
        adjacencyList = {i: [] for i in range(numCourses)}
        visited = set()
        
        for course, prerequisite in prerequisites:
            adjacencyList[course].append(prerequisite)

        for course in range(numCourses):
            if not dfs(course):
                return False
        
        return True
                
            
        
    

