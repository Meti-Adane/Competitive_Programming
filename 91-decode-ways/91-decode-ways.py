class Solution:
    def numDecodings(self, s: str) -> int:
        dp = {len(s):1}
        def decode(i):
            if i in dp:
                return dp[i]
            if s[i] == '0':
                return 0 
            elif i+1 < len(s) and int(s[i:i+2]) <= 26:
                dp[i] = decode(i+1) + decode(i+2)
            else:
                dp[i] = decode(i+1)
            
            return dp[i]
        
        return decode(0)