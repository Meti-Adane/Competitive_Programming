class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        
        ans = []
        def helper(index):
            if index == len(nums):
                ans.append(nums.copy())
                return ans
            arr = []
            for i in range(index, len(nums)):
                nums[i], nums[index] = nums[index], nums[i]
                helper(index+1)
                nums[index], nums[i] = nums[i], nums[index]
            return ans
        
        return helper(0)
        
        