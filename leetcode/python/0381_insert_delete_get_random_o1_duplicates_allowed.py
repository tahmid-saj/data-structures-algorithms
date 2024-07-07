class RandomizedCollection:

    def __init__(self):
        self.map = defaultdict(set)
        self.list = []

    def insert(self, val: int) -> bool:
        i = len(self.list)

        if val in self.map:
            self.map[val].add(i)
            self.list.append(val)
            return False
        elif val not in self.map:
            self.map[val].add(i)
            self.list.append(val)

        return True

    def remove(self, val: int) -> bool:
        if val not in self.map: return False

        i, last = self.map[val].pop(), self.list[-1]

        if i == len(self.list) - 1:
            if len(self.map[val]) == 0: self.map.pop(val)
            self.list.pop()
        else:
            if len(self.map[val]) == 0: self.map.pop(val)
            print(i, len(self.list) - 1)
            self.list[i], self.list[-1] = self.list[-1], self.list[i]
            self.map[last].discard(len(self.list) - 1)
            self.map[last].add(i)
            self.list.pop()

        return True

    def getRandom(self) -> int:
        return random.choice(self.list)


# Your RandomizedCollection object will be instantiated and called as such:
# obj = RandomizedCollection()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()