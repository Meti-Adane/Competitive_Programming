class Solution:
    def countSubstrings(self, s: str) -> int:
        dp = dict()
        N = len(s)
       
        def isPalindrome(word):
            left, right = 0, len(word)-1
            while left < right:
                if word[right] != word[left]: return False 
                left += 1
                right -= 1
            return True 

        def recurse(start, end):
            if (end-start) <= 0 or (start, end) in dp: return 0 
            count = 1 if isPalindrome(s[start:end+1]) else 0 
            dp[(start, end)] = count + recurse(start+1, end) + recurse(start, end-1)
            return dp[(start, end)]
        
        return recurse(0, N-1) + N
       
