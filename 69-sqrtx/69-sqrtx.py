class Solution:
    def mySqrt(self, x: int) -> int:
        
        def helper(start, end, target):
            mid = (end + start) / 2
            if (mid ** 2) // 1 == target:
                return mid 
            if mid ** 2 > target:
                return helper(start, mid, target)
            return helper(mid, end, target)
        
        return int(helper(0, x, x)) 
        