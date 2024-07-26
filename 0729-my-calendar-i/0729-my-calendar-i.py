class MyCalendar(object):

    def __init__(self):
        self.calender = []

    def book(self, start, end):
        """
        :type start: int
        :type end: int
        :rtype: bool
        """
        l = 0
        r = len(self.calender)

        while l < r:
            m = (l + r) // 2

            if self.calender[m][0] <= start:
                l = m + 1
            else:
                r = m
        
        if self.intersection(l, start, end):
            return False
        else:
            self.calender.insert(l, [start, end])
        return True

    def intersection(self, idx, s, e):
        return (self.calender[idx-1][1] > s if idx >= 1 else False) or (self.calender[idx][0] < e if idx < len(self.calender) else False)
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)