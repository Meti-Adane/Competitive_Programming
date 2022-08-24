class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        def helper(n):
       
            if n == 1:
                return True
            if n % 3:
                return False
            return helper(n/3)
        
        return False if n == 0 else helper(n)