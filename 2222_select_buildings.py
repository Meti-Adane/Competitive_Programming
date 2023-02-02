class Solution:
    def numberOfWays(self, s: str) -> int:
        zeros = countedZeros = ones = countedOnes = ans = 0

        for char in s:
            if char == '1':
                ones += 1
            else:
                zeros += 1
            
        for char in s:
            if char == '0':
                ans += (countedOnes * (ones - countedOnes))
                countedZeros += 1
            else:
                ans += (countedZeros * (zeros - countedZeros))
                countedOnes += 1
                
        return ans