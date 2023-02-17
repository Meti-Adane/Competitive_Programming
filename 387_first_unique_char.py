class Solution:
    def firstUniqChar(self, s: str) -> int:
        counter = defaultdict(int)
        
        for letter in s:
            counter[letter] += 1
            
        for pos, letter in enumerate(s):
            if counter[letter] == 1:
                return pos
        return -1
                