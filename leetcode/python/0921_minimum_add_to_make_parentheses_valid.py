class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        # return self.greedy(s)
        return self.stack(s)

    def greedy(self, s):
        openPs, closePs = 0, 0

        for i in range(len(s)):
            if s[i] == "(": closePs += 1
            elif s[i] == ")" and closePs > 0: closePs -= 1
            else: openPs += 1
        
        return openPs + closePs
    
    def stack(self, s):
        stk = []
        openPs = 0

        for i in range(len(s)):
            if s[i] == "(": stk.append(s[i])
            elif s[i] == ")" and stk and stk[-1]: stk.pop()
            else: openPs += 1
        
        return len(stk) + openPs