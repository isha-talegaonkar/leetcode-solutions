class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1 or not edges:
            return [0]
        adjacencyList = defaultdict(list)
        for n1, n2 in edges:
            adjacencyList[n1].append(n2)
            adjacencyList[n2].append(n1)
        
        edgeCount = {}
        leaves = deque()
        
        for node, edges in adjacencyList.items():
            if len(edges) == 1:
                leaves.append(node)
            edgeCount[node] = len(edges)
        
        while leaves:
            if n <= 2:
                return list(leaves)
            for i in range(len(leaves)):
                leafNode = leaves.popleft()
                n -= 1
                
                for neighbor in adjacencyList[leafNode]:
                    edgeCount[neighbor] -= 1
                    if edgeCount[neighbor] == 1:
                        leaves.append(neighbor)
                
            