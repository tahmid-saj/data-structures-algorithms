class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        # if s > n: return
        # if s == n: self.res.append(list(comb)), return
        # loop through (num, 10) using nm:
        #   if s + nm > n: return
        #   if len(comb) < k:
        #       comb.append(nm)
        #       self.backtrack(k, n, comb, s + nm, nm + 1)
        #       comb.pop()
        #   else: return
        self.res = []
        self.backtrack(k, n, [], 0, 1)
        return self.res
    
    def backtrack(self, k, n, comb, s, num):
        if s > n: return
        if s == n and len(comb) == k:
            self.res.append(list(comb))
            return
        
        for nm in range(num, 10):
            if s + nm > n: return
            if len(comb) < k:
                comb.append(nm)
                self.backtrack(k, n, comb, s + nm, nm + 1)
                comb.pop()
            else: return