class Solution:
    def __init__(self):
        self.memo = {}
    def rob(self, nums: List[int]) -> int:
        self.memo = {}
        return self.robFrom(0, nums)
    
    def robFrom(self, pos, nums):
        if pos >= len(nums):
            return 0
        
        if pos in self.memo:
            return self.memo[pos]

        ans = max(self.robFrom(pos+1, nums), self.robFrom(pos+2, nums)+nums[pos])
        
        self.memo[pos] = ans
        
        return ans