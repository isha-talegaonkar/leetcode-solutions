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
        