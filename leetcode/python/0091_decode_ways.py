class Solution:
    def numDecodings(self, s: str) -> int:
        # return self.recursive(s, -1, 0)
        
        # return self.recursive2(s, 0)

        # dp = [-1 for _ in range(len(s))]
        # return self.recursiveTopDown(s, -1, 0, dp)

        # dp = [0 for _ in range(len(s) + 1)]
        # return self.bottomUp(s, dp)

        return self.bottomUpConstantSpace(s)

    def recursive(self, s, index, digits):
        if index > len(s): return 0
        if index == len(s): return 1
        if index != -1 and s[index] == "0": return 0
        if digits != 0 and s[index:index + digits].isnumeric() and (int(s[index:index + digits]) < 1 or int(s[index:index + digits]) > 26): return 0

        res = 0
        if digits < 2: 
            res += self.recursive(s, index + 1, 1)
            if index + 2 < len(s): res += self.recursive(s, index + 1, 2)
        elif digits == 2:
            res += self.recursive(s, index + 2, 1)
            if index + 2 < len(s): res += self.recursive(s, index + 2, 2)

        return res
    
    def recursive2(self, s, index):
        if index > len(s): return 0
        if index == len(s): return 1
        if s[index] == "0": return 0
        if index == len(s) - 1: return 1

        res = self.recursive2(s, index + 1)
        if int(s[index:index + 2]) > 0 and int(s[index:index + 2]) <= 26: res += self.recursive2(s, index + 2)

        return res

    def recursiveTopDown(self, s, index, digits, dp):
        if index > len(s): return 0
        if index == len(s): return 1
        if index != -1 and s[index] == "0": return 0
        if digits != 0 and s[index:index + digits].isnumeric() and (int(s[index:index + digits]) < 1 or int(s[index:index + digits]) > 26): return 0

        if digits < 2:
            if dp[index] == -1:
                dp[index] = self.recursiveTopDown(s, index + 1, 1, dp)
                if index + 2 < len(s): dp[index] += self.recursive(s, index + 1, 2)
        if digits == 2:
            if dp[index] == -1:
                dp[index] = self.recursiveTopDown(s, index + 2, 1, dp)
                if index + 2 < len(s): dp[index] += self.recursive(s, index + 2, 2)
        
        return dp[index]
    
    def bottomUp(self, s, dp):
        if len(s) == 1 and s[0] == "0": return 0
        if len(s) == 1: return 1
        
        dp[0] = 1
        if s[0] != "0": dp[1] = 1

        for i in range(2, len(s) + 1):
            if s[i - 1] != "0": dp[i] = dp[i - 1]

            twoDigit = s[i - 2:i]
            if int(twoDigit) >= 10 and int(twoDigit) <= 26: dp[i] += dp[i - 2]
        
        return dp[len(s)]
    
    def bottomUpConstantSpace(self, s):
        if len(s) == 1 and s[0] == "0": return 0
        if len(s) == 1: return 1
        if s[0] == "0": return 0

        twoPrev, onePrev = 1, 1
        for i in range(2, len(s) + 1):
            curr = 0
            if s[i - 1] != "0": curr = onePrev

            twoDigit = s[i - 2:i]
            if int(twoDigit) >= 10 and int(twoDigit) <= 26: curr += twoPrev
            twoPrev = onePrev
            onePrev = curr
        
        return curr