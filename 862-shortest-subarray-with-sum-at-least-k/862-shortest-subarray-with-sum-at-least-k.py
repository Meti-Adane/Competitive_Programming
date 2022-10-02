class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        que = deque()
        ans, curr_sum = len(nums)+1, 0
        for i, val in enumerate(nums):
            curr_sum += val
            if curr_sum >= k:
                ans = min(ans, i+1)
           
            while que and curr_sum <= que[-1][0]:
                que.pop()
            que.append([curr_sum, i])
            while que and curr_sum - que[0][0] >= k:
                ans = min(ans, i-que.popleft()[1])
                
        return ans if ans <= len(nums) else -1