# question url: https://leetcode.com/problems/maximize-sum-of-array-after-k-negations/

class Solution:
    def largestSumAfterKNegations(self, A: List[int], K: int) -> int:
        #         always choose the smallest one for operation
        arr = A
        heapq.heapify(arr)

        for _ in range(K):
            num = heapq.heappop(arr)
            heapq.heappush(arr, num * -1)
        return sum(arr)