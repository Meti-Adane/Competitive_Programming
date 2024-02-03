class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
       
        N = len(arr)
        
        # dp = dict()
        @cache
        def recurse(index):
            if index >= N: return 0 
            # if index in dp: return dp[index]
            maxCandidate = arr[index]
            maxSum = maxCandidate

            for i in range(index, min(N, index+k)):
                maxCandidate = max(maxCandidate, arr[i])
                subarraySum = (maxCandidate * (i-index+1) ) + recurse(i+1)
                maxSum = max(maxSum, subarraySum)
            # dp[index] = maxSum
            return maxSum


        return recurse(0)

        
