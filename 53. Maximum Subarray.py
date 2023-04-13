class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = float('-inf')
        subarraysum =  float('-inf')
        
        for num in nums:
            if num > subarraysum + num:
                subarraysum = num
            else:
                subarraysum += num
            ans = max(subarraysum, ans)
        return ans