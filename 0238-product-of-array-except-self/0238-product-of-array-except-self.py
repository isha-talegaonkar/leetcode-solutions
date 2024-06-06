class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        answer = [0] * len(nums)
        answer[0] = 1
        
        for i in range(1, len(nums)):
            answer[i] = answer[i-1] * nums[i-1]
        current = 1
        for i in reversed(range(len(nums))):
            answer[i] = answer[i] * current
            current *= nums[i]
            
        return answer
            