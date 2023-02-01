class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        ans = currPlantTime = 0 
        for growth, plant in sorted(zip(growTime, plantTime), reverse=True):
            currPlantTime += plant
            ans = max(ans, growth+currPlantTime)
        return ans 