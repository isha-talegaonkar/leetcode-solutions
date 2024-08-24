class Solution:
    def __init__(self):
        self.memo = []
        self.nums = []
        
    def isJumpPossible(self, currentPosition) -> bool:
        if self.memo[currentPosition] != -1:
            return self.memo[currentPosition] == 1
        
        furthestJump = min(currentPosition + self.nums[currentPosition], len(self.nums) - 1)
        
        for nextPosition in range(currentPosition+1, furthestJump+1):
            if self.isJumpPossible(nextPosition):
                self.memo[currentPosition] = 1
                return True
        self.memo[currentPosition] = 0
        return False
        
        
    def canJump(self, nums: List[int]) -> bool:
        self.memo =[-1] * len(nums)
        self.memo[-1] = 1
        self.nums = nums
        return self.isJumpPossible(0)