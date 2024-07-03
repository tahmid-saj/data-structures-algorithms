class Node:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Bucket:
    def __init__(self):
        self.head = Node(0)
    
    def add(self, key):
        if not self.exists(key):
            newNode = Node(val=key, next=self.head.next)
            self.head.next = newNode
            return

    def remove(self, key):
        prev, curr = self.head, self.head.next
        while curr:
            if curr.val == key: 
                prev.next = curr.next
                return
            prev = curr
            curr = curr.next
    
    def exists(self, key):
        curr = self.head.next
        while curr:
            if curr.val == key: return True
            curr = curr.next
        return False

class MyHashSet:
    def __init__(self):
        self.keySpace = 769
        self.set = [Bucket() for _ in range(self.keySpace)]
    
    def hashFunction(self, key):
        return key % self.keySpace

    def add(self, key: int) -> None:
        index = self.hashFunction(key)
        self.set[index].add(key)

    def remove(self, key: int) -> None:
        index = self.hashFunction(key)
        self.set[index].remove(key)

    def contains(self, key: int) -> bool:
        index = self.hashFunction(key)
        return self.set[index].exists(key)


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)