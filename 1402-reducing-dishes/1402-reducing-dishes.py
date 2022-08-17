class Solution:
    def maxSatisfaction(self, nums: List[int]) -> int:
       
        nums.sort()
        ans = 0 
        for i, num in enumerate(nums):
            currsum = num
            coff = 2
            for j in range(i+1, len(nums)):
                currsum += (coff * nums[j])
                coff += 1
            ans = max(ans, currsum)
        return ans                