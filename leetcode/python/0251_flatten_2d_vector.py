class Vector2D:

    def __init__(self, vec: List[List[int]]):
        # self.vec = []
        # self.i = 0
        # for item in vec:
        #     if item is int: self.vec.append(item)
        #     else:
        #         for val in item: self.vec.append(val)
        self.i = 0
        self.j = 0
        self.vec = vec

    def next(self) -> int:
        # res = self.vec[self.i]
        # self.i += 1
        # return res
        self.correctPosition()
        res = self.vec[self.i][self.j]
        self.j += 1
        return res

    def hasNext(self) -> bool:
        # if self.i == len(self.vec): return False
        # return True
        self.correctPosition()
        return self.i < len(self.vec)
    
    def correctPosition(self):
        while self.i < len(self.vec) and self.j == len(self.vec[self.i]):
            self.i += 1
            self.j = 0

# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(vec)
# param_1 = obj.next()
# param_2 = obj.hasNext()