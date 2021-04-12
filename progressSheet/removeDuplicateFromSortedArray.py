# question url : https://leetcode.com/problems/remove-duplicates-from-sorted-array/

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        for pos in range(len(nums)-1, 0, -1):
            if nums[pos] == nums[pos-1]:
                del nums[pos]