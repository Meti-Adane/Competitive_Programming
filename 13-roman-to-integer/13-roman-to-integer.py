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
        
        while i < len(s):
            if s[i] == 'I' and (i + 1 < len(s)) and (s[i+1] == 'V' or s[i+1] == 'X'):
                integer += (hashMap[s[i+1]] - hashMap[s[i]])
                i += 2
            elif  s[i] == 'X' and (i + 1 < len(s)) and (s[i+1] == 'L' or s[i+1] == 'C'):
                integer += (hashMap[s[i+1]] - hashMap[s[i]])
                i += 2
            elif s[i] == 'C' and (i + 1 < len(s)) and (s[i+1] == 'D' or s[i+1] == 'M'):
                integer += (hashMap[s[i+1]] - hashMap[s[i]])
                i += 2
            else:
                integer += hashMap[s[i]]
                i += 1
                
        return integer
                