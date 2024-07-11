class Solution:
    def simplifyPath(self, path: str) -> str:
        stk = []
        path = path.split("/")

        print(path)

        for i in range(len(path)):
            if path[i] == "" or path[i] == ".": continue
            if path[i] == ".." and len(stk) > 0: stk.pop()
            else: 
                if path[i] != "..": stk.append(path[i])
        
        return "/" + "/".join(stk)