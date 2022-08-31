class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        precedence = dict()
        
        for i, char in enumerate(order):
            precedence[char] = i
            
        for i in range(1, len(words)):
            word1_length, word2_length = len(words[i-1]), len(words[i])
            isSorted = False
            for j in range(min(word1_length, word2_length)):
                if j >= word2_length or j >= word1_length:
                    break;
                if precedence[words[i-1][j]] < precedence[words[i][j]]:
                    isSorted = True
                    break
                if precedence[words[i-1][j]] > precedence[words[i][j]]:
                    return False
            if not isSorted and word1_length > word2_length:
                return False
        
        return True