class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        currentSum = 0
        count = 0
        prefixsums = defaultdict(int)
        
        for i in range(len(nums)):
            currentSum += nums[i]
            if currentSum == k:
                count += 1
            diff = currentSum - k
            if diff in prefixsums:
                count += prefixsums[diff]
            
            prefixsums[currentSum] += 1
        
        return count
        
#         count = 0
        
#         for start in range(len(nums)):
#             subarraySum = 0
#             for end in range(start, len(nums)):
#                 subarraySum += nums[end]
#                 if subarraySum == k:
#                     count += 1 
#         return count
                
#         count = 0
#         for i in range(len(nums)):
#             for j in range(i + 1, len(nums) + 1):
#                 subarraySum = 0
#                 for t in range(i, j):
#                     subarraySum += nums[t]
#                 if subarraySum == k: 
#                     count += 1
        
#         return count