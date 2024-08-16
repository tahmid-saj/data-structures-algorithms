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
        self.backtrack(s, 0, "", 0)
        return self.res
    
    def backtrack(self, s, index, comb, digits):
        if index == len(s) and digits == 4:
            self.res.append(str(comb[:-1]))
            return
        if digits > 4 or index >= len(s): return

        # one digit
        sub = s[index:index + 1]
        self.backtrack(s, index + 1, comb + sub + ".", digits + 1)

        # two digits
        sub = s[index:index + 2]
        if sub[0] != "0": self.backtrack(s, index + 2, comb + sub + ".", digits + 1)

        # three digits
        sub = s[index:index + 3]
        if sub[0] != "0" and int(sub) >= 0 and int(sub) <= 255: self.backtrack(s, index + 3, comb + sub + ".", digits + 1)

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