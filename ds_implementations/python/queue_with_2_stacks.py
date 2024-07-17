class Queue:
  def __init__(self):
    self.enqueue = []
    self.dequeue = []
    self.front = None
  
  def push(self, x):
    if len(self.enqueue) == 0: self.front = x
    self.enqueue.append(x)
  
  def pop(self):
    if len(self.dequeue) == 0:
      while self.enqueue: self.dequeue.append(self.enqueue.pop())
    return self.dequeue.pop()

  def peek(self):
    if len(self.dequeue) != 0: return self.dequeue[-1]
    return self.front

  def isEmpty(self):
    return len(self.enqueue) == 0 and len(self.dequeue) == 0