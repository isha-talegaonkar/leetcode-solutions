class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        unique_numbers = sorted(set(num for lst in nums for num in lst))
        max_value = min(lst[-1] for lst in nums)
        
        unique_numbers = [num for num in unique_numbers if num <= max_value]
        result = [0, math.inf]
        
        for left in unique_numbers:
            min_numbers = []
            for lst in nums:
                min_value = min(num for num in lst if num >= left)
                min_numbers.append(min_value)
            right = max(min_numbers)
            
            if right - left < result[1] - result[0]:
                result = left, right
        
        return result
