class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        hashMap = Counter(words)
        lenOfWord = len(words[0])
        lenOfPhrase = len(words) * lenOfWord
        left = 0
        ans = []
        while left + lenOfPhrase <= len(s):
            isValidPhrase = True
            lookUp = hashMap.copy()
            j = left
            while j < left + lenOfPhrase:
                word = s[j:j+lenOfWord]
                if word not in lookUp or lookUp[word] <= 0:
                    isValidPhrase = False
                    break 
                lookUp[word] -= 1
                j += lenOfWord
                
            if isValidPhrase:
                ans.append(left)
            
            left += 1
            
        return ans
        
    
    
       