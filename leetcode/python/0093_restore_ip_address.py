class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        # if index == len(s): self.res.append(comb[:-1]), return
        # loop through (index, len(s)) using i:
        #   comb += s[i] + ".", self.backtrack(s, comb, i + 1), comb = comb[:-2]
        #   if s[i] != "0":
        #       comb += s[i:i + 2] + ".", self.backtrack(s, comb, i + 2), comb = comb[:-3]
        #       if int(s[i:i + 3]) <= 255:
        #           comb += s[i:i + 3] + ".", self.backtrack(s, comb, i + 3), comb = comb[:-4]

        self.res = []
        self.backtrack(s, 0, [])
        return self.res
    
    def backtrack(self, s, index, comb, digits):
        if index == len(s) and len(comb) == 4:
            self.res.append("".join(comb)[:-1])
            return
        if index >= len(s): return
        if len(comb) >= 4: return

        # single digit
        comb.append(s[index] + ".")
        self.backtrack(s, index + 1, comb)
        comb.pop()

        # double digits
        num = s[index: index + 2]
        if num[0] != "0":
            comb.append(num + ".")
            self.backtrack(s, index + 2, comb)
            comb.pop()
        
        # triple digits
        num = s[index: index + 3]
        if num[0] != "0" and 0 <= int(num) <= 255:
            comb.append(num + ".")
            self.backtrack(s, index + 3, comb)
            comb.pop()

    def iterative(self, s):
        res = []
        queue = [("", 0, 0)]


        while queue:
            comb = queue.pop(0)

            if comb[2] > 4: continue

            if comb[1] + 1 <= len(s):
                oneDigit = str(comb[0] + s[comb[1]] + ".")

                if comb[2] + 1 == 4 and comb[1] + 1 == len(s): res.append(str(oneDigit[:-1]))
                else: queue.append((oneDigit, comb[1] + 1, comb[2] + 1))

                if s[comb[1]] != "0" and comb[1] + 2 <= len(s):
                    twoDigit = str(comb[0] + s[comb[1]:comb[1] + 2] + ".")

                    if comb[2] + 1 == 4 and comb[1] + 2 == len(s): res.append(str(twoDigit[:-1]))
                    else: queue.append((twoDigit, comb[1] + 2, comb[2] + 1))

                    if int(s[comb[1]:comb[1] + 3]) <= 255 and comb[1] + 3 <= len(s):
                        threeDigit = str(comb[0] + s[comb[1]:comb[1] + 3] + ".")

                        if comb[2] + 1 == 4 and comb[1] + 3 == len(s): res.append(str(threeDigit[:-1]))
                        else: queue.append((threeDigit, comb[1] + 3, comb[2] + 1))
                    else: continue
                else: continue
            else: continue

        return res