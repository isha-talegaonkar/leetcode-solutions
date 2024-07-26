class MyCalendar:

    def __init__(self):
        self.calendar = []

    def book(self, start: int, end: int) -> bool:
#         for s, e in self.calendar:
#             if s < end and start < e:
#                 return False
            
#         self.calendar.append((start, end))
#         return True
        left = 0
        right = len(self.calendar)
        
        while left < right:
            middle = left + (right - left) // 2
            
            if self.calendar[middle][0] <= start:
                left = middle + 1
            else:
                right = middle
        
        if self.intersection(left, start, end):
            return False
        
        self.calendar.insert(left, [start, end])
        return True
        
    
    def intersection(self, idx, s, e):
        return (self.calendar[idx-1][1] > s if idx >= 1 else False) or (self.calendar[idx][0] < e if idx < len(self.calendar) else False)


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)