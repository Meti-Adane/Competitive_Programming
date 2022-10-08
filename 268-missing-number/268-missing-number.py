class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        xor = 0 
        
        for i in range(len(nums)+1):xor ^= i
        
        for num in nums: xor ^= num
        return xor
            
            