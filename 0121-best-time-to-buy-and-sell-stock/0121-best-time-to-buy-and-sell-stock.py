class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice = float("inf")
        maxProfit = 0
        
        for i in range(len(prices)):
            if minPrice > prices[i]:
                minPrice = prices[i]
            elif maxProfit < prices[i] - minPrice:
                maxProfit = prices[i] - minPrice
        
        return maxProfit
                
                