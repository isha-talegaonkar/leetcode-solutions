class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        n = len(nums)
        left = 0
        right = n - 1
        
        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] > nums[n - 1]:
                left = mid + 1
            else:
                right = mid - 1
        
        def binarySearch(left_b, right_b, target):
            left, right = left_b, right_b
            while left <= right:
                mid = left + (right - left) // 2
                
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
                
            return -1
        
        if (answer := binarySearch(0, left-1, target)) != -1:
            return answer
        
        return binarySearch(left, n - 1, target)