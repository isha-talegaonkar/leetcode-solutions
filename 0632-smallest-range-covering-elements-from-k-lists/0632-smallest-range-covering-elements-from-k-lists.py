class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        unique_numbers = sorted(set(num for lst in nums for num in lst))
        max_value = min(lst[-1] for lst in nums)

        unique_numbers = [num for num in unique_numbers if num <= max_value]
        result_range = [0, math.inf]

        for left in unique_numbers:
            min_values = []
            for lst in nums:
                min_value = (min(num for num in lst if num >= left))
                min_values.append(min_value)
            right = max(min_values)

            if right - left < result_range[1] - result_range[0]:
                result_range = [left, right]

        return result_range
