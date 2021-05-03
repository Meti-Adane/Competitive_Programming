# question url : https://leetcode.com/problems/find-k-closest-elements/

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        collector = []
        output=[]
        for num in arr:
            collector.append((abs(num-x), num))
        heapq.heapify(collector)

        for i in range(k):
            output.append(heapq.heappop(collector)[1])
        output.sort()
        return output