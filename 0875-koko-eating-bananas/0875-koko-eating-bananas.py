class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
#         speed = 1
        
#         while True:
#             current_k = 0
#             for pile in piles:
#                 current_k += math.ceil(pile/speed)
            
#             if current_k <= h:
#                 return speed
#             else:
#                 speed += 1

        left = 1
        right = max(piles)
        
        while left < right:
            current_k = 0
            middle = (left + right) // 2
            for pile in piles:
                current_k += math.ceil(pile/middle)
            if current_k <= h:
                right = middle
            else:
                left = middle + 1
        return right
                
                
                        
            
        