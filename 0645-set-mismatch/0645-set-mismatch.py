class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        duplicate, missing = None, None
        
        for num in nums:
            if nums[abs(num)-1] < 0:
                duplicate = abs(num)
            else:
                nums[abs(num)-1] = nums[abs(num)-1] * -1
                
        for pos, num in enumerate(nums):
            if num > 0:
                return [duplicate, pos+1]
            
            