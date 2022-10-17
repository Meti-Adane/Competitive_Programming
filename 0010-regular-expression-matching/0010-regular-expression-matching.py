class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s = list(s)
        p = list(p)
        memo =dict()
        
        def matchExpression(si, pi):
            if (si, pi) in memo:
                return memo[(si, pi)]
            if si >= len(s) and pi >= len(p):
                return True 
            if pi >= len(p):
                return False
            
            match = si < len(s) and (p[pi] == '.' or s[si]==p[pi])
            
            if pi+1 < len(p) and p[pi+1] == '*':
                memo[(si, pi)] = (match and matchExpression(si+1, pi)) or (matchExpression(si, pi+2))
                return memo[(si, pi)]
            if match:
                memo[(si, pi)]= matchExpression(si+1, pi+1)
                return memo[(si, pi)]
            memo[(si, pi)] =  False
            return memo[(si, pi)]
        
        return matchExpression(0, 0)