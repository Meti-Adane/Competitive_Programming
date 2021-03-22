# questionurl : https://leetcode.com/problems/simplify-path/
class Solution:
    def simplifyPath(self, path: str) -> str:
        rtr = re.split('/', path)
        outputpath = []

        for i in range(len(rtr)):
            if rtr[i] == "..":
                if outputpath:
                    outputpath.pop()
            elif rtr[i] == "" or rtr[i] == ".":
                continue
            else:
                outputpath.append(rtr[i])
        return "/" + "/".join(outputpath)
