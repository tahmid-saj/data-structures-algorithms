class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stk = []
        # traverse through s using i:
        # -> if s[i] == "(" or s[i] == "[" or s[i] == "{": stk.append(s[i])
        # -> elif s[i] == ")" and stk[-1] == "(": stk.pop()
        # -> elif s[i] == "]" and stk[-1] == "[": stk.pop()
        # -> elif s[i] == "}" and stk[-1] == "{": stk.pop()
        # -> else: return False
        # return True
        for i in range(len(s)):
            if s[i] == "(" or s[i] == "[" or s[i] == "{": stk.append(s[i])
            elif (s[i] == ")" or s[i] == "]" or s[i] == "}") and not stk: return False 
            elif s[i] == ")" and stk[-1] == "(": stk.pop()
            elif s[i] == "]" and stk[-1] == "[": stk.pop()
            elif s[i] == "}" and stk[-1] == "{": stk.pop()
            else: return False
        return not stk