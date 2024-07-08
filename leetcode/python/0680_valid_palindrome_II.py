class Solution:
    def validPalindrome(self, s: str) -> bool:
        i, j = 0, len(s) - 1

        while i <= j:
            if s[i] != s[j]:
                return self.isPalindrome(s, i) or self.isPalindrome(s, j)
            else:
                i += 1
                j -= 1
        
        return True
    
    def isPalindrome(self, s, ignore):
        i, j = 0, len(s) - 1

        while i <= j:
            if i == ignore: 
                i += 1
                continue
            elif j == ignore: 
                j -= 1
                continue
                
            if s[i] != s[j]: return False
            i += 1
            j -= 1
        
        return True