class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        # Flatten all lists into a single set and sort them
        unique_numbers = sorted(set(num for lst in nums for num in lst))

        # Find the smallest max value of the last elements in each list
        max_value = min(lst[-1] for lst in nums)

        # Trim unique numbers to those less than or equal to max_value
        unique_numbers = unique_numbers[:bisect.bisect_right(unique_numbers, max_value)]

        # Initialize the smallest range
        result_range = [0, math.inf]

        # Iterate over all possible left boundaries
        for left in unique_numbers:
            # Find the right boundary for each list that is >= left
            right = max(lst[bisect.bisect_left(lst, left)] for lst in nums)

            # Update the result if the current range is smaller
            if right - left < result_range[1] - result_range[0]:
                result_range = [left, right]

        return result_range
#         minx = 0
#         miny = float('inf')
#         max_val = float('-inf')
#         next_idx = [0] * len(nums)
#         flag = True
        
#         min_heap = []
#         for i in range(len(nums)):
#             heapq.heappush(min_heap, (nums[i][0], i))
#             max_val = max(max_val, nums[i][0])
        
#         while flag:
#             min_val, min_idx = heapq.heappop(min_heap)
#             if miny - minx > max_val - min_val:
#                 minx = min_val
#                 miny = max_val
            
#             next_idx[min_idx] += 1
#             if next_idx[min_idx] == len(nums[min_idx]):
#                 flag = False
#                 break
            
#             next_val = nums[min_idx][next_idx[min_idx]]
#             heapq.heappush(min_heap, (next_val, min_idx))
#             max_val = max(max_val, next_val)
        
#         return [minx, miny]