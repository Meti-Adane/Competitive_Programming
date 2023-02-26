class Solution:
    def numSquarefulPerms(self, nums: List[int]) -> int:
        
        ans = []
        nums.sort()
        
        def dfs(nums, path, ans):
            if not nums:
                ans.append(path)
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i-1]:
                    continue 
                if path and not pow(sqrt(int(path[-1]+nums[i])), 2) == int(path[-1]+nums[i]):
                    continue 
                dfs(nums[:i]+nums[i+1:], path+[nums[i]], ans)
            
            return len(ans)
        
        return dfs(nums, [], ans)