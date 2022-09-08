class Solution:
    def longestValidParentheses(self, s: str) -> int:
        left, right, maxlen = 0, 0, 0
        
        
        for char in s:
            if char == "(":
                left += 1
            else:
                right += 1
            
            if left == right:
                maxlen = max(maxlen, left+right)
            if right > left:
                left, right = 0, 0
                
        left , right = 0, 0
        for i in range(len(s)-1, -1, -1):
            if s[i] == "(":
                left += 1
            else:
                right += 1
            if left == right:
                maxlen = max(maxlen, left+right)
            if left > right:
                left, right = 0, 0 
        
        
        return maxlen
                
                    
                    