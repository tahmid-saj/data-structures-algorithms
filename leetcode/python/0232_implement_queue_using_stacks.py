class MyQueue(object):
    def __init__(self):
        self.enqueue = []
        self.dequeue = []
        self.front = None

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        if len(self.enqueue) == 0: self.front = x
        self.enqueue.append(x)

    def pop(self):
        """
        :rtype: int
        """
        if len(self.dequeue) == 0:
            while self.enqueue: self.dequeue.append(self.enqueue.pop())
        return self.dequeue.pop()

    def peek(self):
        """
        :rtype: int
        """
        if self.dequeue: return self.dequeue[-1]
        return self.front

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.enqueue) == 0 and len(self.dequeue) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()