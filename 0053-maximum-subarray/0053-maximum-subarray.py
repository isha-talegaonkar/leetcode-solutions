class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxSum = nums[0]
        sumSoFar = 0
        
        for n in nums:
            if sumSoFar < 0:
                sumSoFar = 0
            sumSoFar += n
            maxSum = max(maxSum, sumSoFar)
        
        return maxSum
        