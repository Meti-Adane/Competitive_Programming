class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        a,b,c = len(nums)-3, len(nums)-2, len(nums)-1
        
        while a >= 0 :
            res =  nums[a] + nums[b] + nums[c]
            if nums[a] + nums[b] > nums[c]:
                return res
            a -= 1
            b -= 1
            c -= 1
        return 0 