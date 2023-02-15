class Solution:
    def numSquarefulPerms(self, nums: List[int]) -> int:
        
        ans = []
        nums.sort()
        self.dfs(nums, [], ans)
        return len(ans)
    
    def dfs(self, nums, path, ans):
        if not nums:
            ans.append(path)
        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                continue 
            if path and not self.square(path[-1]+nums[i]):
                continue 
            self.dfs(nums[:i]+nums[i+1:], path+[nums[i]], ans)
        
    def square(self, x):
        from math import sqrt
        return pow(int(sqrt(x)), 2) == x