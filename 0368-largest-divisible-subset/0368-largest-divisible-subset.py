class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        N = len(nums)
        dp = [list([nums[i]]) for i in range(N)]
        maxLength, index = 0, -1

        for i in range(N):
            for j in range(0, i):
                if nums[i] % nums[j] == 0 and len(dp[j])+1 > len(dp[i]):
                    dp[i] = dp[j].copy() + [nums[i]]

            if len(dp[i]) > maxLength:
                maxLength, index = len(dp[i]), i

        return dp[index]

                