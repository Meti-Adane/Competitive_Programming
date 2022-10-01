class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        prefixsum = [0]
        left, ans = 0, len(nums)+1
        for val in (nums):
            prefixsum.append(prefixsum[-1]+val)
        
        for i, cumulative_sum in enumerate(prefixsum):
            while (cumulative_sum - prefixsum[left]) >= target:
                ans = min(ans, i-left)
                left += 1
        return ans if ans <= len(nums) else 0 
        
        