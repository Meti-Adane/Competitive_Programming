class Solution:
    def numSplits(self, s: str) -> int:
        uniqueChars= [0 for _ in range(len(s))]
        hashmap = set()
        count = 0 

        for i, char in enumerate(s):
            hashmap.add(char)
            uniqueChars[i] = len(hashmap)
        
        hashmap = set()
        for i in range(len(s)-1, -1, -1):
            hashmap.add(s[i])
            if i-1 >= 0 and uniqueChars[i-1] == len(hashmap):
                count += 1
            uniqueChars[i] = len(hashmap)
        return count