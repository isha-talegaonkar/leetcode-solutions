class MyCalendar:

    def __init__(self):
        self.calendar = []

    def book(self, start: int, end: int) -> bool:
        left = 0
        right = len(self.calendar)
        
        while left < right:
            mid = left + (right-left) // 2
            
            if self.calendar[mid][0] <= start:
                left = mid + 1
            else:
                right = mid
            
        if self.intersects(left, start, end):
            return False
        
        self.calendar.insert(left, [start, end])
        return True

    def intersects(self, index, start, end):
        return ((index >= 1 and self.calendar[index-1][1] > start) or (index < len(self.calendar) and self.calendar[index][0] < end))
        
# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)