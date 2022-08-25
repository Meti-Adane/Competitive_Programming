class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hashMap = Counter(magazine)
        
        for char in ransomNote:
            if char not in hashMap or hashMap[char] <= 0:
                return False
            hashMap[char] -= 1
        return True