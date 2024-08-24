class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adjecencyList = defaultdict(list)
        indegree = {}
        for dest, src in prerequisites:
            adjecencyList[src].append(dest)
            indegree[dest] = indegree.get(dest, 0) + 1
        
        queue = deque(k for k in range(numCourses) if k not in indegree)
        order = []
        print(indegree)
        while queue:
            course = queue.pop()
            order.append(course)
            for neighbor in adjecencyList[course]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)
        
        return order if len(order) == numCourses else []
            