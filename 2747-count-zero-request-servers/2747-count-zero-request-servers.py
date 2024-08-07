from collections import defaultdict

class Solution:
    def countServers(self, n: int, logs: List[List[int]], x: int, queries: List[int]) -> List[int]:
        queries = [(i, q-x, q) for i, q in enumerate(queries)]
        queries.sort(key = lambda x:x[1])
        
        logs.sort(key = lambda x: x[1])
        logs.append([0, float("inf")])
        
        activeServers = defaultdict(int)
        inactiveServers = [0] * len(queries)
        
        right, left = 0, 0
        
        for i, start, end in queries:
            while logs[right][1] <= end and right<len(logs):
                activeServers[logs[right][0]] = activeServers[logs[right][0]] + 1
                right += 1
            
            while logs[left][1] < start and left<len(logs):
                activeServers[logs[left][0]] -= 1
                if activeServers[logs[left][0]] == 0:
                    del activeServers[logs[left][0]]
                left += 1
            
            inactiveServers[i] = n - len(activeServers)
        
        return inactiveServers
            
            