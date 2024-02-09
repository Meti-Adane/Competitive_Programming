class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        prefix = [0] 
        suffix = [0]
        N = steps = len(nums)

        for i in range(N):
            prefix.append(prefix[-1] + nums[i])
            suffix.append(suffix[-1] + nums[N-i-1])

        
        minSteps = N+1
        for i, cummulativeSum in enumerate(prefix):
            if cummulativeSum > x: break
            target = x-cummulativeSum
            idx = bisect_left(suffix, target)
            if idx <= N and suffix[idx] == target:
                minSteps = min(minSteps, (i+idx))
        
        return -1 if minSteps >= N+1 else minSteps 