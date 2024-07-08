class Logger:

    def __init__(self):
        self.logs = {}
        self.time = 10

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        if message not in self.logs: 
            self.logs[message] = timestamp
            return True
        else:
            if timestamp - self.logs[message] >= self.time:
                self.logs[message] = timestamp
                return True
        return False

# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)