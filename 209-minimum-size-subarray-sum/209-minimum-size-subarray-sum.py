class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        prefixsum = 0
        left, ans = 0, len(nums)+1
        for r, val in enumerate(nums):
            prefixsum += val
            while prefixsum >= target:
                ans = min(ans, r-left+1)
                prefixsum -= nums[left]
                left += 1
        return ans if ans <= len(nums) else 0
        