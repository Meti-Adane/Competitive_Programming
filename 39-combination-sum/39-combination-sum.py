class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        def combine(index, runningSum, stack, combinations):
            if runningSum == target:
                combinations.append(stack.copy())
                return combinations
            if runningSum > target or index >= len(nums):
                return combinations


            stack.append(nums[index])
            combinations = combine(index, runningSum+nums[index], stack, combinations)
            stack.pop()
            combinations = combine(index+1, runningSum, stack, combinations)
            return combinations

        return combine(0, 0, [], [])