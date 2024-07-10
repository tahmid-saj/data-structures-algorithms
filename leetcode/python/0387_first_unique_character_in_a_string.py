class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq = {}
        for i in range(len(s)):
            if s[i] not in freq: freq[s[i]] = (i, 1)
            else: freq[s[i]]= (freq[s[i]][0], freq[s[i]][1] + 1)
        
        for i, v in freq.items():
            if v[1] == 1: return v[0]
        
        return -1