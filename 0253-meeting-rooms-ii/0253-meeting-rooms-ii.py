class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        
        if not intervals:
            return 0
        intervals.sort(key=lambda x: x[0])
        
        meetingRooms = []
        heapq.heappush(meetingRooms, intervals[0][1])
        
        for interval in intervals[1:]:
            startTime = interval[0]
            
            if meetingRooms[0] <= startTime:
                heapq.heappop(meetingRooms)
            
            heapq.heappush(meetingRooms, interval[1])
        
        return len(meetingRooms)
        