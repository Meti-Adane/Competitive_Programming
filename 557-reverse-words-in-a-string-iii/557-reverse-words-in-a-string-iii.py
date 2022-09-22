class Solution:
    def reverseWords(self, s: str) -> str:
        ans = []
        words = s.split()
        
        def reverseWord(word, ans):
            l, r = 0, len(word)-1
            container = list(word)
            while l < r:
                container[l], container[r] = container[r], container[l]
                l += 1
                r -= 1
            ans.extend(container)
            
            
        for word in words:
            reverseWord(word, ans)
            ans.append(" ")
        ans.pop()
        return "".join(ans)
  
        
        