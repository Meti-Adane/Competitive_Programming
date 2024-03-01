class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        count = s.count('1')
        return '1'*(count-1) + (len(s)-count) * '0' + '1'