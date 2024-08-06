class MyCalendarTwo:
    def __init__(self):
        self.intervals = []

    def book(self, start: int, end: int) -> bool:
        if not self.intervals:
            self.intervals.append((start, 1))
            self.intervals.append((end, -1))
            return True

        temp = self.intervals.copy()
        temp.append((start, 1))
        temp.append((end, -1))
        temp.sort()
        need = 0
        for _, delta in temp:
            need += delta
            if need == 3:
                return False

        self.intervals.append((start, 1))
        self.intervals.append((end, -1))
        return True


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(start,end)