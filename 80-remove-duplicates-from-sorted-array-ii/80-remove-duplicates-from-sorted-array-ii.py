class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        place, count, prev = None, 0, None
        
        for i, num in enumerate(nums):
            if num != prev:
                prev = num
                count = 0
            count += 1
            if place and count <= 2:
                nums[i], nums[place] = nums[place], nums[i]
                place += 1
            if not place and count > 2:
                place = i
            
            
        return place