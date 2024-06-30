class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self.i = -1
        self.j = -1
        self.curr = None
        self.v1 = v1
        self.v2 = v2

    def next(self) -> int:
        if self.curr == 0: res = self.v1[self.i]
        else: res = self.v2[self.j]
        return res

    def hasNext(self) -> bool:
        self.correctPosition()
        if self.curr == None: return False
        elif self.curr == 0: return self.i < len(self.v1)
        return self.j < len(self.v2)
    
    def correctPosition(self):
        if self.curr == None:
            if len(self.v1) == 0 and len(self.v2) == 0: self.curr = None
            elif len(self.v1) == 0: 
                self.curr = 1
                self.j += 1
            elif len(self.v2) == 0: 
                self.curr = 0
                self.i += 1
            else: 
                self.curr = 0
                self.i += 1
        elif self.curr == 0:
            if self.j != len(self.v2) - 1:
                self.curr = 1
                self.j += 1
            else: self.i += 1
        elif self.curr == 1:
            if self.i != len(self.v1) - 1:
                self.curr = 0
                self.i += 1
            else: self.j += 1

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())