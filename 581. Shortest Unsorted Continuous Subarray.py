class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        start, end = len(nums), float('-inf')    
        stack = []
        for pos, num in enumerate(nums): # get start pos
            while stack and stack[-1][0] > num:
                start = min (start, stack.pop()[1])
            stack.append((num, pos))
        
        stack = []
        for i in range(len(nums)-1, -1, -1): #get end pos 
            while stack and stack[-1][0] < nums[i]:
                end = max(end, stack.pop()[1])
            stack.append((nums[i], i))
            
        return end-start+1 if start < len(nums) else 0