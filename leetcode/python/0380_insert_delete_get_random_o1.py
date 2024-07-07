class RandomizedSet:
    
    def __init__(self):
        self.map = {}
        self.list = []

    def insert(self, val: int) -> bool:
        if val in self.map: return False

        i = len(self.list)
        self.list.append(val)
        self.map[val] = i
        return True

    def remove(self, val: int) -> bool:
        if val not in self.map: return False

        i, j = self.map[val], len(self.list) - 1
        self.map[self.list[j]] = i
        self.list[i], self.list[j] = self.list[j], self.list[i]
        self.list.pop()
        self.map.pop(val)
        return True

    def getRandom(self) -> int:
        return random.choice(self.list)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()