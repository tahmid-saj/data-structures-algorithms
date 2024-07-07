class MinStack:

    def __init__(self):
        self.stk = []
        self.min = []
        
    def push(self, val: int) -> None:
        self.stk.append(val)
        if len(self.min) == 0 or self.min[-1][0] > val: self.min.append((val, 1))
        elif self.min[-1][0] == val: self.min[-1] = (val, self.min[-1][1] + 1)

    def pop(self) -> None:
        val = self.stk.pop()
        if self.min[-1][0] == val: 
            if self.min[-1][1] == 1: self.min.pop()
            else: self.min[-1] = (val, self.min[-1][1] - 1)

    def top(self) -> int:
        return self.stk[-1]

    def getMin(self) -> int:
        return self.min[-1][0]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()