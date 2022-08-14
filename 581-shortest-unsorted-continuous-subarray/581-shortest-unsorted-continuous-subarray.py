class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        stack = []
        start, end = float('inf'), -1
        for i, num in enumerate(nums):
            while stack and stack[-1][0] > num:
                start = min(start, stack.pop()[1])
            stack.append([num, i])
            
        stack = []
        
        for i in range(len(nums)-1, -1, -1):
            while stack and stack[-1][0] < nums[i]:
                end = max(end, stack.pop()[1])
            stack.append([nums[i], i])
            
        return 0 if start > len(nums) else end - start +1 