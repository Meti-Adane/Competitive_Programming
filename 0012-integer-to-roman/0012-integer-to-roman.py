# 9:47 : 9:58 : 03 : 10
class Solution:
    def intToRoman(self, num: int) -> str:
        romans = [(1000,  'M'),  
                  (900,   "CM"),
                  (500,   "D"),
                  (400,   "CD"),
                  (100,   "C"),
                  (90 ,   "XC"),
                  (50,    "L"),
                  (40,    "XL"),
                  (10,    "X"),
                  (9,     "IX"), 
                  (5,     "V"),
                  (4,     "IV"), 
                  (1,     "I") ]
        x = num 
        romanIdx = 0
        ans = []
        
        while x >= 1:
            if x >= romans[romanIdx][0]:
                ans.append(romans[romanIdx][1])
                x -= romans[romanIdx][0]
            else:
                romanIdx += 1
        return "".join(ans)
    
    
   