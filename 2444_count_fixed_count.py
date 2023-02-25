class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        min_val,max_val,count,start = -1,-1,0,0
        for i in range(len(nums)):
            if(nums[i] < minK or nums[i] > maxK):
                start = i+1
                min_val = max_val = -1

            if(nums[i] == minK): min_val = i
            if(nums[i] == maxK): max_val = i
            if(max_val != -1 and min_val != -1):
                count += (i - start + 1) - (i - (min(max_val,min_val)))
        return count