class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        seen, palindromes, count = dict(), [], 0
        hasPivotPalindrome = lambda arr, hashmap : any([ hashmap[w] % 2 == 1 for w in arr ])
        
        for word in words:
            if word[0] == word[1]:
                palindromes.append(word)
            seen[word] = seen.get(word, 0) + 1
            
        pivot = 2 if hasPivotPalindrome(palindromes, seen) else 0

        for word, freq in seen.items():
            reverse = word[::-1]
            x = y = 0
            if reverse == word:
                y = 2
                x = seen[word] if seen[word] % 2 == 0 else seen[word] - 1
                
            elif reverse in seen:
                x = min(seen[word], seen[reverse])
                y = 4
                seen[reverse] = 0 
            
            count += (x*y)
            seen[word] = 0
           
        return count + pivot 