class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        lastBuilding = len(heights) -1
        heap = []
        
        for i, height in enumerate(heights):
            if bricks < 0: return i-1
            if i == lastBuilding: return i 
            gap = heights[i+1] - height
            bricks -= max(gap, 0) 
            heapq.heappush(heap, -1*gap)
            if ladders >= 1 and bricks < 0:
                highestgap = -1 * heapq.heappop(heap)
                ladders -= 1
                bricks += highestgap

        return lastBuilding

            
                
            



