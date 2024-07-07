from collections import OrderedDict
class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.freq = 1
        self.prev = self.next = None

class DLL:
    def __init__(self):
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.head.prev = self.tail.next = None
        self.size = 0
    
    def __len__(self):
        return self.size

    def add(self, node):
        prevHead = self.head.next
        prevHead.prev = node
        node.next = prevHead

        node.prev = self.head
        self.head.next = node
        self.size += 1
    
    def remove(self, node):
        if self.size == 0: return
        prev = node.prev
        nxt = node.next
        prev.next = nxt
        nxt.prev = prev

        self.size -= 1
        return node

class LFUCache:
    def __init__(self, capacity: int):
        # self.freq = defaultdict(DLL)
        # self.lfu = {}
        # self.capacity = capacity
        # self.minFreq = 0
        self.cache = {}
        self.frequencies = defaultdict(OrderedDict)
        self.minf = 0
        self.capacity = capacity
    
    def insert(self, key, frequency, value):
        self.cache[key] = (frequency, value)
        self.frequencies[frequency][key] = value

    def get(self, key: int) -> int:
        # if key not in self.lfu: return -1

        # node = self.lfu[key]
        # freq = node.freq
        # self.freq[freq].remove(node)

        # if len(self.freq[freq]) == 0:
        #     del self.freq[freq]
        #     if freq == self.minFreq: self.minFreq += 1
        
        # node.freq += 1
        # self.freq[node.freq].add(node)
        # self.lfu[key] = node
        # return node.val
        if key not in self.cache: return -1
        frequency, value = self.cache[key]
        del self.frequencies[frequency][key]

        if not self.frequencies[frequency]:
            del self.frequencies[frequency]
            if frequency == self.minf: self.minf += 1

        self.insert(key, frequency + 1, value)

        return value

    def put(self, key: int, value: int) -> None:
        # if self.capacity == 0: return
        # if key in self.lfu:
        #     self.lfu[key].val = value
        #     self.get(key)
        #     return
        
        # if len(self.lfu) == self.capacity:
        #     dll = self.freq[self.minFreq]
        #     n = self.freq[self.minFreq].remove(dll.tail.prev)
        #     del self.lfu[n.key]
        
        # node = Node(key, value)
        # self.freq[1].add(node)
        # self.lfu[key] = node
        # self.minFreq = 1
        if self.capacity <= 0: return
        if key in self.cache:
            frequency = self.cache[key][0]
            self.cache[key] = (frequency, value)
            self.get(key)
            return

        if self.capacity == len(self.cache):
            key_to_delete, frequency = self.frequencies[self.minf].popitem(last=False)
            del self.cache[key_to_delete]

        self.minf = 1
        self.insert(key, 1, value)


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)