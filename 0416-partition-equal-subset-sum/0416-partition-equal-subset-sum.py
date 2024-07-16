class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if(sum(nums) % 2):
            return False
        dp = set()
        dp.add(0)
        
        target = sum(nums) // 2
        
        for i in range(0, len(nums)):
            newDp = set()
            for t in dp:
                newDp.add(t + nums[i])
                newDp.add(t)
            dp = newDp
        
        return True if target in dp else False
        