from collections import defaultdict

class OrderedSet:
    def __init__(self):
        self.orderedset = []
    
    def add(self, element):
        for e in self.orderedset:
            if element[0] == e[0]:
                k = self.orderOfKey(element)
                self.orderedset[k][1] += element[1]
                self.orderedset.sort(key=lambda x: x[0])
                return
        self.orderedset.append(element)
        self.orderedset.sort(key=lambda x: x[0])
    
    def findByOrder(self, k):
        if k < 0 or k >= len(self.orderedset): return None
        return self.orderedset[k]
    
    def orderOfKey(self, element):
        return sum(1 for x in self.orderedset if x[0] < element[0])

class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        # return self.orderedSet(items1, items2)
        return self.orderedDict(items1, items2)

    def orderedSet(self, items1, items2):
        orderedset = OrderedSet()
        maxLength = max(len(items1), len(items2))
        for i in range(maxLength):
            if i < len(items1): orderedset.add(items1[i])
            if i < len(items2): orderedset.add(items2[i])
        
        return orderedset.orderedset
    
    def orderedDict(self, items1, items2):
        merged = defaultdict(int)

        for v, w in items1: merged[v] += w
        for v, w in items2: merged[v] += w

        return sorted([[v, w] for v, w in merged.items()], key=lambda x: x[0])