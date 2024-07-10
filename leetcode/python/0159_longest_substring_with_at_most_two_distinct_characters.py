class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        if len(s) < 3: return len(s)
        res, letters, start = 0, {}, 0
        for end in range(len(s)):
            letters[s[end]] = letters.get(s[end], 0) + 1

            while len(letters) > 2:
                if letters[s[start]] == 1: letters.pop(s[start])
                else: letters[s[start]] -= 1
                start += 1
            res = max(res, end - start + 1)
        
        return res