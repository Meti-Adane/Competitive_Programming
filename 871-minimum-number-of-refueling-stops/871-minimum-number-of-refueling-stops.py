class Solution(object):
    def minRefuelStops(self, target, tank, stations):
        heap = []  
        stations.append((target, float('inf')))

        ans = prev = 0
        for location, capacity in stations:
            tank -= location - prev
            while heap and tank < 0:
                tank += -heapq.heappop(heap)
                ans += 1
            if tank < 0: return -1
            heapq.heappush(heap, -capacity)
            prev = location

        return ans