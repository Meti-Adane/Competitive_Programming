class Solution:
    def validUtf8(self, data: List[int]) -> bool:
        byte = n = 0
        
        for num in data:
            binaryStr = bin(num)[2:]
            if n > 0:
                if len(binaryStr) < 8 or binaryStr[:2] != '10': return False
                n -= 1
            else:
                if len(binaryStr) >= 8:
                    byte = n = 0
                    for bit in binaryStr:
                        if bit == '0': break
                        byte += 1
                    if byte > 4 or byte < 2: return False
                    n = byte - 1
                else:
                    byte = n =0 

        return n == 0