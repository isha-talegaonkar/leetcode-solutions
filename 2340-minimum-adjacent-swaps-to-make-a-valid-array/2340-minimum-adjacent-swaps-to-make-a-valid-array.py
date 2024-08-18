class Solution:
    def minimumSwaps(self, nums: List[int]) -> int:
        min_num = float("inf")
        min_index = 0
        
        max_num = float("-inf")
        max_index = 0
        
        for i in range(len(nums)):
            if nums[i] < min_num:
                min_num = nums[i]
                min_index = i
            
            if nums[i] >= max_num:
                max_num = nums[i]
                max_index = i
        
        print("max: ", max_num, max_index)
        print("min: ", min_num, min_index)
        
        #number of swaps to move the min number to the left: min_index
        #number of swaps to move the max number to the right: (len(nums)  - max_index - 1)
        #min swaps: left swaps + right swaps
        
        res = min_index + (len(nums)  - max_index - 1)
        
        #edge case for when the min_index also gets swapped during the right_index swap
        if min_index > max_index:
            res -= 1
        
        return res
        