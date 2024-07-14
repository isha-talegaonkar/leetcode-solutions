class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        frequencies = Counter(tasks)
        
        maxHeap = [-freq for freq in frequencies.values()]
        heapq.heapify(maxHeap)
        
        queue = deque()
        time = 0
        while maxHeap or queue:
            time += 1
            if maxHeap:
                task = 1 + heapq.heappop(maxHeap)
                if task:
                    queue.append([task, time + n])
            if queue and queue[0][1] == time:
                heapq.heappush(maxHeap, queue.popleft()[0])
        return time
            
            
            
        