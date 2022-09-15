class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        l, r = 0, len(nums)
        
        while l < r:
            mid = (l+r) // 2
            
            if mid == nums[mid]:
                l = mid + 1
            if mid < nums[mid]:
                r = mid 
        return r
        