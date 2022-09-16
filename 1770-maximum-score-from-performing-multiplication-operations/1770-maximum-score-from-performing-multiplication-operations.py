class Solution:
    def maximumScore(self, nums: List[int], mult: List[int]) -> int:
        n, m = len(nums), len(mult)
        dp = [0 for _ in range(m+1)]
        
        for i in range(m-1, -1, -1):
            for j in range(i+1):
                dp[j] = max(
                    nums[j]*mult[i] + dp[j+1],
                    nums[n-1 - (i-j)]*mult[i] + dp[j]
                )
        return dp[0]