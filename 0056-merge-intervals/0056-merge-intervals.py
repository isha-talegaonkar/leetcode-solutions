class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key = lambda x: x[0])
        
        mergedIntervals = []
        
        for interval in intervals:
            if not mergedIntervals or mergedIntervals[-1][1] < interval[0]:
                mergedIntervals.append(interval)
            else:
                mergedIntervals[-1][1] = max(mergedIntervals[-1][1], interval[1])
        
        return mergedIntervals