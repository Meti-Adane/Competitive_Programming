class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        
        
        def helper(nums):
            if not len(nums) or len(nums) == 1:
                return [nums]
            
            arr = []
            for i in range(len(nums)):
                num = nums[i]
                for p in helper(nums[:i]+nums[i+1:]):
                    arr.append([num] + p)
            return arr
        
        return helper(nums)
        
        