class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        
        result = 0
        total = 0
        for i in range(len(gas)):
            total += gas[i] - cost[i]
            
            if total < 0:
                total = 0
                result = i+1
            
        return result
        
#         totalGain = 0
#         currentGain = 0
        
#         result = 0
        
#         for i in range(len(gas)):
#             totalGain += gas[i] - cost[i]
#             currentGain += gas[i] - cost[i]
            
#             if currentGain < 0:
#                 result = i + 1
#                 currentGain = 0
        
#         return result if totalGain >= 0 else -1