from heapq import *
from sortedcontainers import SortedList
class MaxStack:

    def __init__(self):
        # self.maxHeap = []
        # self.stk = []
        # self.deleted = set()
        # self.i = 0
        self.stk = SortedList()
        self.max = SortedList()
        self.i = 0

    def push(self, x: int) -> None:
        # self.stk.append((x, self.i))
        # heappush(self.maxHeap, (-x, -self.i))
        # self.i += 1
        self.stk.add((self.i, x))
        self.max.add((x, self.i))
        self.i += 1

    def pop(self) -> int:
        # while self.stk and self.stk[-1][1] in self.deleted: self.stk.pop()
        # res = self.stk.pop()
        # if -self.maxHeap[0][1] == res[1]: heappop(self.maxHeap)
        # else: self.deleted.add(res[1])
        # return res[0]
        i, val = self.stk.pop()
        self.max.remove((val, i))
        return val

    def top(self) -> int:
        # while self.stk and self.stk[-1][1] in self.deleted: self.stk.pop()
        # return self.stk[-1][0]
        return self.stk[-1][1]

    def peekMax(self) -> int:
        # while self.maxHeap and -self.maxHeap[0][1] in self.deleted: heappop(self.maxHeap)
        # return -self.maxHeap[0][0]
        return self.max[-1][0]

    def popMax(self) -> int:
        # while self.maxHeap and -self.maxHeap[0][1] in self.deleted: heappop(self.maxHeap)
        # res = heappop(self.maxHeap)
        # if -res[1] == self.stk[-1][1]: self.stk.pop()
        # else: self.deleted.add(-res[1])
        # return -res[0]
        val, i = self.max.pop()
        self.stk.remove((i, val))
        return val

# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()