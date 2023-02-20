class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        
        ans = 0 
        def helper(word) :
            i = j = 0
            while i < len(s) and j < len(word) and s[i] == word[j]:
                count_s = count_word = 1
                while i + count_s < len(s) and s[i] == s[i+count_s]:
                        count_s+=1
                while j + count_word < len(word) and word[j] == word[j+count_word]:
                        count_word +=1
                i, j = i+count_s, j+count_word
                if count_word < count_s < 3 or count_word > count_s: 
                    return 0				
            return 1 if i == len(s) and j == len(word) else 0
        
        for word in words:
             ans += helper(word)
        return ans