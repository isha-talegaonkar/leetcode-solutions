class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        def squaredDistance(point):
            return point[0] ** 2 + point[1] ** 2
        
        heap = []
        
        for i in range(k):
            heap.append((-squaredDistance(points[i]), i))
        heapq.heapify(heap)
        
        for i in range(k, len(points)):
            distance = -squaredDistance(points[i])
            if distance > heap[0][0]:
                heapq.heappop(heap)
                heapq.heappush(heap, (distance, i))
        
        return [points[i] for( _, i) in heap]
                
        