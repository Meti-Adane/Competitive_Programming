class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        ans = []
        candidates.sort()
        
        def helper(idx, path, runningSum):
            nonlocal ans
            
            if runningSum == target:
                ans.append(path.copy())
            if runningSum > target:
                return ans
            prev = -1
            for i in range(idx, len(candidates)):
                if candidates[i] == prev:
                    continue 
                path.append(candidates[i])
                helper(i+1, path, runningSum+candidates[i])
                path.pop()
                prev= candidates[i]
            return ans
        return helper(0, [], 0)
