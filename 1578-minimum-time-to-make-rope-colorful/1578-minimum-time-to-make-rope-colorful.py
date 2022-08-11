class Solution:
    def minCost(self, s: str, neededTime: List[int]) -> int:
        ans = left = 0 
        
        while left < len(s):
            maxEffort = totalEffort = neededTime[left]
            isEffortRequired = False
            right = left + 1
            while right < len(neededTime) and s[right] == s[left]:
                isEffortRequired = True
                totalEffort += neededTime[right]
                maxEffort = max(maxEffort, neededTime[right])
                right += 1
            if isEffortRequired:
                ans += (totalEffort - maxEffort)
            left = right
            
        return ans
            
            