class Solution:
    def numSub(self, s: str) -> int:
        dp = dict()
        dp[1] = 1
        
        left = right = 0 
        ans = 0
        mod = pow(10, 9) + 7
        
        while left < len(s):
            onescount = 0
            right = left
            while right < len(s) and s[left] == s[right] == "1":
                onescount += 1
                right += 1
             
            if onescount:
                ans += self.countsubstring(onescount, dp)
                left = right 
            else:
                left += 1
                
        return ans % mod
    
    def countsubstring(self, n, dp):
        if n in dp:
            return dp[n]
        if n == 0:
            return 0
        dp[n] = self.countsubstring(n-1, dp) + n   
        return dp[n]


        