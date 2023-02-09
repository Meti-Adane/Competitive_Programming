class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ans = []
        
        def backtrack(s, dotcount, path):
            if not dotcount:
                if len(s) >=2 and s[0] == '0':
                    return 
                if (s and int(s) <= 255):
                    ans.append("".join([s]+path))
                return 
            if not dotcount or not s:
                return 
                     
            backtrack(s[:-1], dotcount-1, [".", s[-1]]+path)
            
            if len(s) >= 2 and s[-2] != "0":
                backtrack(s[:-2], dotcount-1, [".", s[-2:]]+path)
           
            if len(s) >= 3 and (s[-3] == "1" or (s[-3]=="2" and int(s[-3:]) <= 255)):
                backtrack(s[:-3], dotcount -1, [".", s[-3:]]+path)
          
        backtrack(s, 3, [])
        return ans
                                
                                
                
                
            
            
        
        