
class Solution:
    def longestObstacleCourseAtEachPosition(self, obstacles: List[int]) -> List[int]:
        
        ans = []
        dp = [float('inf')] * (len(obstacles)+1)
        
        
        def binary_search_lower(low, high, target):
            index = 0
            
            while low <= high:
                mid = (low+high) // 2
                
                if dp[mid] <= target:
                    index = max(mid+1, index)
                    low = mid + 1
                else:
                    high = mid -1
            return index
        
        
        for i in range(len(obstacles)):
            index = binary_search_lower(0, len(dp)-1, obstacles[i])
            dp[index] = obstacles[i]
            ans.append(index+1)
        return ans
            
            
            
            