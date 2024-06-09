class Solution:
    def generateAbbreviations(self, word: str) -> List[str]:
        self.res = []
        self.backtrack(word, 0, [])
        return self.res
    
    def backtrack(self, word, index, comb):
        if index == len(word):
            self.res.append("".join(comb))
            return

        comb.append(str(word[index]))
        self.backtrack(word, index + 1, comb)
        comb.pop()

        for i in range(index, len(word)):
            if (len(comb) > 0 and not comb[-1].isnumeric()) or len(comb) == 0:
                abbreviation = len(word[index: i + 1])
                comb.append(str(abbreviation))
                self.backtrack(word, i + 1, comb)
                comb.pop()