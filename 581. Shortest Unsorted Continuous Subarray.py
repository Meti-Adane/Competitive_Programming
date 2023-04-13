# Method 1 sorting 
class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        high, low = -1, -1 
        arr = sorted(nums)
        for i in range(len(nums)):
            if nums[i] != arr[i] and low == -1:
                low = i 
            if nums[i] != arr[i] and low > -1:
                high = i
        return high - low + 1 if low > -1 else 0



# Method 2 monotonic stacks
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