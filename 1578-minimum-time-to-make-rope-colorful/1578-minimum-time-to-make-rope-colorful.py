class Solution:
    def minCost(self, s: str, neededTime: List[int]) -> int:
        ans = left = 0 
        while left < len(s):
            maxEffort = totalEffort = neededTime[left]
            right = left + 1
            while right < len(neededTime) and s[right] == s[left]:
                totalEffort += neededTime[right]
                maxEffort = max(maxEffort, neededTime[right])
                right += 1
            ans += (totalEffort - maxEffort)
            left = right
            
        return ans
            
            