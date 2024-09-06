class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        heap = []
        curr_max = float('-inf')
        for i in range(len(nums)):
            heappush(heap, [nums[i][0], i, 0])
            curr_max = max(curr_max, nums[i][0])
        
        best_max = curr_max
        best_min = heap[0][0]
        
        while len(heap) == len(nums):
            val, i, j = heappop(heap)
            if j+1 >= len(nums[i]):
                continue
            
            heappush(heap, [nums[i][j+1], i, j+1])
            curr_min = heap[0][0]
            curr_max = max(curr_max, nums[i][j+1])
            
            if curr_max - curr_min < best_max - best_min:
                best_min, best_max = curr_min, curr_max
            
        
        return [best_min, best_max]
            