class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.index = defaultdict(list)
        for i in range(len(wordsDict)):
            self.index[wordsDict[i]].append(i)

    def shortest(self, word1: str, word2: str) -> int:
        index1, index2 = self.index[word1], self.index[word2]
        i, j, res = 0, 0, math.inf
        while i < len(index1) and j < len(index2):
            res = min(res, abs(index1[i] - index2[j]))
            if index1[i] < index2[j]: i += 1
            elif index1[i] > index2[j]: j += 1
            else: return 0
        return res

# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)