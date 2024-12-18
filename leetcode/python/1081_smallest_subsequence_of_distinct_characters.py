class Solution:
    def smallestSubsequence(self, s: str) -> str:
        # set to record elements already added onto stack, lastOccurence to record last index of s[i], monotonic inc (a b c) stack
        seen, stk, lastOccurence = set(), [], {}

        for i in range(len(s)): lastOccurence[s[i]] = i

        for i in range(len(s)):
            if s[i] not in seen:
                while stk and stk[-1][0] >= s[i]:
                    if i < lastOccurence[stk[-1][0]]:
                        c, _ = stk.pop()
                        if c in seen: seen.remove(c)
                    else: break
                if s[i] not in seen:
                    stk.append((s[i], i))
                    seen.add(s[i])
        
        res = ""
        while stk: res += stk.pop()[0]
        return res[::-1]