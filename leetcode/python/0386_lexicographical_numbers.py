class TrieNode:
    def __init__(self):
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, num):
        node = self.root
        for w in num:
            if w not in node.children: node.children[w] = TrieNode()
            node = node.children[w]

class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        trie = Trie()
        for i in range(1, n + 1): trie.insert(str(i))

        def dfs(n, node, num):
            for k in sorted(node.children.keys()):
                if node.children[k] != None:
                    self.res.append(int(num + k))
                    dfs(n, node.children[k], num + k)

        self.res = []
        dfs(n, trie.root, "")
        return self.res