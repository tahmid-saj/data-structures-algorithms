class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        # return self.splitting(version1, version2)
        return self.withoutSplitting(version1, version2)

    def splitting(self, version1, version2):
        version1 = version1.split(".")
        version2 = version2.split(".")
        i, j = 0, 0
        while i < len(version1) or j < len(version2):
            num1, num2 = 0, 0
            if i < len(version1): num1 = int(version1[i])
            if j < len(version2): num2 = int(version2[i])

            if num1 < num2: return -1
            if num1 > num2: return 1
            i += 1
            j += 1

        return 0

    def withoutSplitting(self, version1, version2):
        i, j = 0, 0
        while i < len(version1) or j < len(version2):
            num1, num2 = 0, 0
            if i < len(version1): i, num1 = self.revision(version1, i)
            if j < len(version2): j, num2 = self.revision(version2, j)

            if num1 < num2: return -1
            if num1 > num2: return 1
        
        return 0
    
    def revision(self, version, i):
        start = i
        while i < len(version) and version[i] != ".": i += 1
        return i + 1, int(version[start:i])