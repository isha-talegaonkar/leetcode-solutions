class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashmap = defaultdict(int)
        
        for num in nums:
            hashmap[num] += 1
        
        heap = []
        heapq.heapify(heap)
        for key, val in hashmap.items():
            if len(heap) < k:
                heapq.heappush(heap, (val, key))
            else:
                if val > heap[0][0]:
                    heapq.heappop(heap)
                    heapq.heappush(heap, (val, key))
        
        res = []
        for key, val in heap:
            res.append(val)
        
        return res