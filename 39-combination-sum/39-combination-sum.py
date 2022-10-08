class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        def recursive():
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
        
        def iterative():
            stack = []
            ans = []
            stack.append((0, 0, []))

            while stack:
                index, runningSum, path = stack.pop()
                if index >= len(nums) or runningSum > target:
                    continue
                if runningSum == target:
                    ans.append(path.copy())
                else:
                    newans = path.copy()
                    stack.append((index, runningSum+nums[index], path.copy() + [nums[index]]))
                    stack.append((index+1, runningSum, path.copy()))
            return ans
        
        #return iterative()
        return recursive()