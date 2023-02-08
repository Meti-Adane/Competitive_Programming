class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        a = b = c = float('-inf')
        seen = set()
        
        for num in nums:
            if num in seen:
                continue 
            seen.add(num)
            if num > c:
                a = b 
                b = c 
                c = num 
            elif num > b:
                a = b 
                b = num 
            elif num > a:
                a = num 
        return a if a != float('-inf') else c