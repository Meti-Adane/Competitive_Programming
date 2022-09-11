class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        arr = sorted(zip(efficiency, speed), reverse=True)
        runningSum, heap, mod = 0, [], 10**9 + 7
        maxPerformance = 0
        
        for eff, spd in arr:
            while len(heap) > k-1: #subtract the extra gn ke min heap sihon I will get minimum values 
                runningSum -= heappop(heap)
            runningSum += spd
            maxPerformance = max(maxPerformance, runningSum * eff)
            heappush(heap, spd)
        return maxPerformance % mod