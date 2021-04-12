# question url : https://leetcode.com/problems/k-closest-points-to-origin/

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        distance = []
        heapq.heapify(distance)
        output = []

        for point in points:
            res = point[0] ** 2 + point[1] ** 2
            heapq.heappush(distance, [res, point])

        for i in range(k):
            output.append(heapq.heappop(distance)[1])

        return output