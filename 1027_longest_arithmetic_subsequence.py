class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        dp = defaultdict(dict)
        ans = 0
        for i in range(len(nums)):
            container = set()
            for j in range(i-1, -1, -1):
                diff = nums[i] - nums[j]
                
                if diff not in container: 
                    
                    container.add(diff)
                    if diff not in dp[j]:
                        dp[j][diff] = 1
                    dp[i][diff] = dp[j][diff] + 1
                    # print(dp[j][diff])
                    # print(dp[i][diff])
                    ans = max(ans, dp[i][diff])
        
        return ans