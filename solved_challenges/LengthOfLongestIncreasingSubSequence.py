# question url  :https://leetcode.com/problems/longest-increasing-subsequence/


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        nums.append(float('INF'))
        memo = [0] * len(nums)

        for right in range(len(nums) - 1, -1, -1):
            for left in range(right, len(nums)):
                if nums[left] > nums[right]:
                    memo[right] = max(memo[right], memo[left] + 1)

        return max(memo)