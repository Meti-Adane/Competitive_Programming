# question url: https://leetcode.com/problems/find-k-pairs-with-smallest-sums/submissions/

import heapq


class Solution:
    def kSmallestPairs(self, nums1, nums2, k):
        res = []
        for i in nums1:
            for j in nums2:
                heapq.heappush(res, [i + j, i, j])

        # heapq.heapify(res)
        realres = []
        for _ in range(k):
            if res:
                realres.append(heapq.heappop(res)[1::])
        print(realres)
        return realres