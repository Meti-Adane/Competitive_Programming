class Solution:
    def validPalindrome(self, s: str) -> bool:
        return self.recurse(s, 0, len(s)-1, 1)
        
        
    def recurse (self, s, i, j, k):
        if i >= j: 
            return True
        if s[i] != s[j] and k == 0:
            return False
        elif s[i] != s[j]:
            k = k - 1 
        
            return self.recurse(s, i+1, j, k) or  self.recurse(s, i, j-1, k) 
        return self.recurse(s, i+1, j-1, k)