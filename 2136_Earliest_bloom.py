class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        ans = 0
        currPlantTime = 0 
        arr = list(zip(growTime, plantTime))
        arr.sort(reverse=True)
        
        for growth, plant in arr:
            currPlantTime += plant
            ans = max(ans, growth+currPlantTime)
        return ans 