class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        
        for x, y in points:
            distance = x**2 + y**2
            heap.append([distance, x, y])
        
        heapq.heapify(heap)
        
        res = []
        while k > 0:
            distance, x, y = heapq.heappop(heap)
            res.append([x,y])
            k -= 1
            
        
        return res

        
            