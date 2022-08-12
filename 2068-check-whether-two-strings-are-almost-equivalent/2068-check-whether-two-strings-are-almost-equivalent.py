class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        counter1 = Counter(word1)
        counter2 = Counter(word2)
        
        for letter in counter1:
            if abs(counter1[letter] - counter2[letter]) > 3:
                return False
        for letter in counter2:
            if abs(counter2[letter] - counter1[letter]) > 3:
                return False
        return True