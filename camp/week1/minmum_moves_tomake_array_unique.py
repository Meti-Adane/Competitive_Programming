class Solution:
    def minIncrementForUnique(self, A: List[int]) -> int:
        nums = A
        nums.sort()
        count = 0
        for i in range (1, len(nums)):
            if nums[i] <= nums[i-1]:
                val = nums[i-1] + 1
                count += val - nums[i]
                nums[i] = val
        return count