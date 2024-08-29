class Solution:
    def candy(self, ratings: List[int]) -> int:
        # left2right = [1] * len(ratings)
        # right2left = [1] * len(ratings)

#         for i in range(1, len(ratings)):
#             if(ratings[i] > ratings[i-1]):
#                 left2right[i] = left2right[i-1] + 1
        
#         for i in range(len(ratings)-2, -1, -1):
#             if(ratings[i] > ratings[i+1]):
#                 right2left[i] = right2left[i+1] + 1
            
#         result = 0
#         for i in range(len(ratings)):
#             result += max(left2right[i], right2left[i])

        candies = [1] * len(ratings)
        
        for i in range(1, len(ratings)):
            if(ratings[i] > ratings[i-1]):
                candies[i] = candies[i-1] + 1
        result = candies[-1]
        for i in range(len(ratings)-2, -1, -1):
            if(ratings[i] > ratings[i+1]):
                candies[i] = max(candies[i+1] + 1, candies[i])
            result += candies[i]
        
        return result