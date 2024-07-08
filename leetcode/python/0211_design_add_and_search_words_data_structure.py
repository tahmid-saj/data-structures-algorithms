class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False  

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def charToIndex(self, ch):
        return ord(ch) - ord('a')

    def addWord(self, word: str) -> None:
        node = self.root
        for w in word:
            i = self.charToIndex(w)
            if i not in node.children: node.children[i] = TrieNode()
            node = node.children[i]
        node.isEnd = True

    def search(self, word: str) -> bool:
        node = self.root
        return self.searchDfs(word, node, 0)
    
    def searchDfs(self, word, node, index):
        if index == len(word) and node.isEnd == True: return True
        if index == len(word) and node.isEnd == False: return False
        if node == False: return False

        if word[index] == ".":
            # try all possible paths
            for k, v in node.children.items():
                if self.searchDfs(word, v, index + 1): return True
        else:
            i = self.charToIndex(word[index])
            if i not in node.children: return False
            if self.searchDfs(word, node.children[i], index + 1): return True
        
        return False


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)