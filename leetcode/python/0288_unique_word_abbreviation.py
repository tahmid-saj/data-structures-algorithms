class ValidWordAbbr:

    def __init__(self, dictionary: List[str]):
        self.abbreviation = defaultdict(set)
        for word in dictionary: self.abbreviation[self.abbreviate(word)].add(word)
    
    def abbreviate(self, word):
        if len(word) <= 2: return word
        return word[0] + str(len(word) - 2) + word[-1]

    def isUnique(self, word: str) -> bool:
        abbreviation = self.abbreviate(word)
        if abbreviation in self.abbreviation:
            if word in self.abbreviation[abbreviation] and len(self.abbreviation[abbreviation]) == 1: return True
            return False
        return True

# Your ValidWordAbbr object will be instantiated and called as such:
# obj = ValidWordAbbr(dictionary)
# param_1 = obj.isUnique(word)