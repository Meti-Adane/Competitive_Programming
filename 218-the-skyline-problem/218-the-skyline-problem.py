class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        changes = [[start, -height, end] for start, end, height in buildings]
        changes += [[end, 0, 0] for start, end, height in buildings]
        changes.sort()
		
        res = [[0, 0]]
        heap = [(0, float('inf'))]

        for start, height, end in changes:
            while heap[0][1] <= start:
                heappop(heap)

            if height:
                heappush(heap, (height, end))

            if res[-1][1] != -heap[0][0]:
                res.append([start, -heap[0][0]])

        return res[1:]