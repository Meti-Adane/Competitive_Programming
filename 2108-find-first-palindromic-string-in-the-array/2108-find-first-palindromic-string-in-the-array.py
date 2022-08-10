class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        
        def isPalindrome(i, j, s):
            if i >= j :
                return True
            
            if s[i] != s[j]:
                return False
            return isPalindrome(i+1, j-1, s)
        
        
        for s in words:
            if isPalindrome(0, len(s)-1, s):
                return s
        return ""