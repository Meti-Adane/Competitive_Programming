class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        ans = [-1 for _ in range(len(nums))]
        arr = sorted([i for i in range(len(nums))], key=lambda x:nums[x])
        prev = arr[-1]
        
        for i in range(len(arr)-2, -1, -1):
            idx = arr[i]
            if idx < prev:
                prev = idx
            else:
                ans[idx] = nums[prev]
        
        stack = []
        for i, val in enumerate(nums):
            while stack and val > nums[stack[-1]]:
                ans[stack.pop()] = nums[i]
            stack.append(i)
        return ans 
    