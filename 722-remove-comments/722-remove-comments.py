#5:07
class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        block = False
        ans = []
        arr=[]
        
        for line in source:
            start = 0 if not block else len(line) 
            limit = False
            i = 0
            while i < len (line) and not limit:
                skip = False
                char = line[i]
                if char == '/' and i+1 < len(line) and not block:
                    if line[i+1] == '/' :
                        limit = True
                        i += 1
                    elif line[i+1] == '*':
                        block = True
                        i+= 1
                elif char == '*' and i+1 < len(line) and line[i+1] == '/' and block:
                    block = False
                    skip = True
                    i += 1
                    
                
                if not block and not limit and not skip: #atleast one char to include 
                    arr.append(line[i])
                i += 1
            if not block and arr:
                ans.append("".join(arr))
                arr=[]
        
        return ans
        