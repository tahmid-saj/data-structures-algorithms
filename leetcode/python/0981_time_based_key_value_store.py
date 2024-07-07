from sortedcontainers import SortedDict
class TimeMap:

    def __init__(self):
        # self.map = defaultdict(list)
        self.map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        # self.map[key].append((timestamp, value))
        if key not in self.map: self.map[key] = SortedDict()
        self.map[key][timestamp] = value

    def get(self, key: str, timestamp: int) -> str:
        # if key not in self.map: return ""
        # l, r = 0, len(self.map[key])
        # if r == -1: return ""
        # if timestamp < self.map[key][0][0]: return ""

        # while l < r:
        #     middle = l + (r - l) // 2
        #     if self.map[key][middle][0] <= timestamp: l = middle + 1
        #     else: r = middle
        # return "" if r == 0 else self.map[key][l - 1][1]
        
        if key not in self.map: return ""
        i = self.map[key].bisect_right(timestamp)
        if i == 0: return ""
        return self.map[key].peekitem(i - 1)[1]

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)