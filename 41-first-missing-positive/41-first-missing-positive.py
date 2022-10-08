class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        
        for i, num in enumerate(nums):
            if num < 0: nums[i] = 0 
        for i, num in enumerate(nums):
            idx_position = abs(num) - 1 # minus one since array is zero based index
            if idx_position >= 0 and idx_position < len(nums):
                nums[idx_position] = abs(nums[idx_position]) * -1 if nums[idx_position] != 0 else abs(num) * -1
        for i in range(len(nums)):
            if nums[i] >= 0:
                return i+1
        return len(nums)+1
            