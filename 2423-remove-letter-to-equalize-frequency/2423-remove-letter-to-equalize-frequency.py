class Solution:
    def equalFrequency(self, word: str) -> bool:
        N = len(word)
        
        for i in range(N):
            counter = Counter(word)
            counter[word[i]] -= 1 # simiulate deleting a char at an index 
            if counter[word[i]] == 0:
                del counter[word[i]] # so i dont count r:0 as a value 
            if len(set(counter.values())) == 1: #every char now has the same freq
                return True
        return False