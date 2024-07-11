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
        self.backtrack(s, "", 0, 0)
        return self.res
    
        # return self.iterative(s)

    def backtrack(self, s, comb, index, digits):
        if digits > 4: return
        if digits == 4 and index == len(s):
            self.res.append(str(comb[:-1]))
            return

        if index + 1 <= len(s):
            comb += s[index] + "."
            digits += 1
            self.backtrack(s, comb, index + 1, digits)
            comb = str(comb[:-2])
            digits -= 1

            if s[index] != "0" and index + 2 <= len(s):
                digits += 1
                comb += s[index:index + 2] + "."
                self.backtrack(s, comb, index + 2, digits)
                comb = str(comb[:-3])
                digits -= 1

                if int(s[index:index + 3]) <= 255 and index + 3 <= len(s):
                    digits += 1
                    comb += s[index:index + 3] + "."
                    self.backtrack(s, comb, index + 3, digits)
                    comb = str(comb[:-4])
                    digits -= 1
                else: return
            else: return
        else: return

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