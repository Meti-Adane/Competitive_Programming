class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        def combine(index, runningSum, stack, combinations):
            if runningSum == target:
                combinations.append(stack.copy())
                return combinations
            if runningSum > target:
                return combinations
            
            for i in range(index, len(nums)):
                stack.append(nums[i])
                combinations = combine(i, runningSum+nums[i], stack, combinations)
                stack.pop()
            return combinations

        return combine(0, 0, [], [])