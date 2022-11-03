class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        seen, count, pivot = Counter(words), 0, False
        
        for word, freq in seen.items():
            reverse = word[::-1]
            if reverse == word:
                pivot |= (freq % 2 == 1)
                count += (2 * (freq if freq % 2 == 0 else freq-1))
            elif reverse in seen:
                count += (4 * min(freq, seen[reverse]))
            seen[word] = 0
        
        return count + 2 if pivot else count