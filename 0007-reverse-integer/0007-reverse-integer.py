class Solution:
    def reverse(self, x: int) -> int:
        ans, sign = 0, 1 
        lbound, ubound = (-2**31), (2**31)-1
        if x < 0:
            sign = -1
            x *= -1
        while x != 0:
            num = x % 10
            x //= 10
            ans = ans * 10 + num
            if ans >= ubound or ans <= lbound:
                return 0
        return ans * sign 