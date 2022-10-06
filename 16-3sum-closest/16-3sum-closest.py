class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        ans = 0 
        proximity = float('inf')
        nums.sort()
        for i, num1 in enumerate(nums):
            left, right = i+1, len(nums)-1
            while left < right:
                res = nums[left] + nums[right] +num1
                if abs(res-target) < proximity:
                    proximity, ans = abs(res-target), res
                if res > target:
                    right -= 1 
                elif res < target:
                    left += 1
                else:
                    break
        return ans