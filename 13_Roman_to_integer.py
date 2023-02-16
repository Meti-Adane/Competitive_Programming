class Solution:
    def romanToInt(self, s: str) -> int:
        hashMap = {
            "I" : 1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        
        integer = 0
        i = 0 
        
        for i in range(len(s)):
            if i + 1 < len(s) and hashMap[s[i]] < hashMap[s[i+1]]:
                integer -=  hashMap[s[i]]
            else:
                integer += hashMap[s[i]]
            
        return integer
                