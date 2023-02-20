class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        
        def helper(s, word) :
            i = j = 0
            while i < len(s) and j < len(word) and s[i] == word[j]:
                count_s = count_word = 1
                while i + count_s < len(s) and s[i] == s[i+count_s]:
                        count_s+=1
                while j + count_word < len(word) and word[j] == word[j+count_word]:
                        count_word +=1
                i, j = i+count_s, j+count_word
                if count_word < count_s < 3 or count_word > count_s: 
                    return False				
            return i == len(s) and j == len(word)
        
        return sum(helper(s, word) for word in words)