"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
from collections import deque

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node
        
        visited = {}
        
        queue = deque([node])
        
        visited[node] = Node(node.val, [])
        
        while queue:
            n = queue.popleft()
            
            for neighbor in n.neighbors:
                if neighbor not in visited:
                    visited[neighbor] = Node(neighbor.val, [])
                
                    queue.append(neighbor)
                visited[n].neighbors.append(visited[neighbor])
        
        return visited[node]