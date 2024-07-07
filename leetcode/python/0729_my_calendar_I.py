from sortedcontainers import SortedList

class MyCalendar:

    def __init__(self):
        # self.bookings = []
        self.bookings = SortedList()

    def book(self, start: int, end: int) -> bool:
        # for s, e in self.bookings:
        #     if s < end and start < e: return False
        # else:
        #     self.bookings.append([start, end])
        #     self.bookings.sort(key=lambda x: x[0])
        #     return True
        i = self.bookings.bisect_right((start, end))
        if (i > 0 and start < self.bookings[i - 1][1]) or (i < len(self.bookings) and self.bookings[i][0] < end): return False
        self.bookings.add((start, end))
        return True


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(start,end)