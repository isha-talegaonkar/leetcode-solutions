# class Solution:
#     def totcount(self, start, end, s):
#         stin = -1
#         endin = -1
#         flag = False
        
#         for i in range(start, end + 1):
#             if s[i] == '|':
#                 if not flag:
#                     stin = i
#                     flag = True
#                 endin = i
        
#         c = 0
#         for i in range(stin, endin + 1):
#             if i != stin and i != endin:
#                 if s[i] == '*':
#                     c += 1
        
#         return c

#     def platesBetweenCandles(self, s, queries):
#         ans = []
#         for query in queries:
#             st = query[0]
#             end = query[1]
            
#             count = self.totcount(st, end, s)
#             if count < 0:
#                 ans.append(0)
#             else:
#                 ans.append(count)
        
#         return ans
class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)

        left_candle = [-1] * n
        right_candle = [-1] * n
        prefix_plates = [0] * n

        nearest_left = -1
        for i in range(n):
            if s[i] == '|':
                nearest_left = i
            left_candle[i] = nearest_left

        nearest_right = -1
        for i in range(n-1,-1,-1):
            if s[i] == '|':
                nearest_right = i
            right_candle[i] = nearest_right

        numPlates = 0
        for i in range(n):
            if s[i] == "*":
                numPlates += 1   
            prefix_plates[i] = numPlates

        ans = []

        for start, end in queries:
            left_bound = right_candle[start]
            right_bound = left_candle[end]

            if left_bound >= right_bound or left_bound < 0 or right_bound >= n:
                ans.append(0)
            else:
                ans.append(prefix_plates[right_bound] - prefix_plates[left_bound])

        return ans
        