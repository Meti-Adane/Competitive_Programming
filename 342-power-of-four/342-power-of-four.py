class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        def power(n):
            if n == 1:
                return True
            if n % 4 :
                return False
            return power(n/4)
        
        if n == 0:
            return False
        
        return power(n)
    