class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        if len(s) < 10: return []
        
        start, res, dnas = 0, set(), {}
        for end in range(9, len(s)):
            dna = s[start:end + 1]
            dnas[dna] = dnas.get(dna, 0) + 1

            if dnas[dna] > 1: res.add(dna)
            start += 1
        
        return list(res)