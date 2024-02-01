class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = dict()
        for pos, num in enumerate(nums):
            if target - num in seen:
                return [seen[target - num], pos]
            seen[num] = pos
