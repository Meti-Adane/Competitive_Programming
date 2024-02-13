class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        
        def isPalindrome(s:str, start:int, end:int):
            if end-start <= 0 : return True 
            return s[start] == s[end] and isPalindrome(s, start+1, end-1)
        
        for word in words:
            if isPalindrome(word, 0, len(word)-1): return word
        return ""