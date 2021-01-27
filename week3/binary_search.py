# question url: https://leetcode.com/problems/binary-search/submissions/
class Solution:
    def search(self, nums: [int], target: int) -> int:
        left = 0
        right = len(nums)
        while left < right:
            mid = (left + right) // 2
            if target < nums[mid]: right = mid
            elif target > nums[mid]: left = mid + 1
            else:
                return nums.index(target)
        return -1