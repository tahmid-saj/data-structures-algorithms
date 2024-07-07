class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # return self.oneHashmap(s, p)
        # return self.twoHashmaps(s, p)
        return self.twoArrays(s, p)

    def oneHashmap(self, s, p):
        freq = {}
        for i in range(len(p)): freq[p[i]] = freq.get(p[i], 0) + 1

        start, res, matched = 0, [], 0
        for end in range(0, len(s)):
            if s[end] in freq: 
                freq[s[end]] -= 1
                if freq[s[end]] == 0: matched += 1
            
            if matched == len(freq): res.append(start)

            if end >= len(p) - 1:
                if s[start] in freq:
                    if freq[s[start]] == 0: matched -= 1
                    freq[s[start]] += 1
                start += 1

        return res
    
    def twoHashmaps(self, s, p):
        freqS, freqP = {}, {}
        for i in range(len(p)): freqP[p[i]] = freqP.get(p[i], 0) + 1

        start, res = 0, []
        for end in range(0, len(s)):
            freqS[s[end]] = freqS.get(s[end], 0) + 1

            if end >= len(p):
                freqS[s[start]] -= 1
                if freqS[s[start]] == 0: freqS.pop(s[start])
                start += 1
            
            if freqS == freqP: res.append(start)
        
        return res
    
    def twoArrays(self, s, p):
        countS, countP = [0 for _ in range(26)], [0 for _ in range(26)]
        for i in range(len(p)): countP[ord(p[i]) - ord('a')] += 1

        start, res = 0, []
        for end in range(0, len(s)):
            countS[ord(s[end]) - ord('a')] += 1

            if end >= len(p):
                countS[ord(s[start]) - ord('a')] -= 1
                if countS[ord(s[start]) - ord('a')] < 0: countS[ord(s[start]) - ord('a')] = 0
                start += 1
            
            if countS == countP: res.append(start)
        
        return res