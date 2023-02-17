class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        Min,Max,Count,Start = -1,-1,0,0
        for i in range(len(nums)):
            if(nums[i] < minK or nums[i] > maxK):
                Start = i+1
                Min = -1
                Max = -1
            if(nums[i] == minK): Min = i
            if(nums[i] == maxK): Max = i
            if(Max != -1 and Min != -1):
                Count += (i - Start + 1) - (i - (min(Max,Min)))
        return Count