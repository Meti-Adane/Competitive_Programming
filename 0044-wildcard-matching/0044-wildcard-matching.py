class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = [False for _ in range(len(p)+1)]
        dp[0] = True 
        
        for j in range(len(p)):
            if p[j] == '*':
                dp[j+1] = dp[j]
        for i in range(len(s)):
            newdp = [False for _ in range(len(p)+1)]
            for j in range(len(p)):
                if p[j] == '*':
                    newdp[j+1] = dp[j+1] or newdp[j]
                else:
                    newdp[j+1] = dp[j] and (s[i] == p[j] or p[j] == '?')
            dp = newdp.copy()
        return dp[-1]
        
       
        
        