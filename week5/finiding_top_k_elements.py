# question url: https://leetcode.com/problems/top-k-frequent-elements/
import collections
import heapq
class Solution:
    def topKFrequent(self, nums: [int], k: int) -> [int]:
        count_dict =  collections.Counter(nums)
        heap = []
        answer = []
        for key, value in count_dict.items():
            heapq.heappush(heap, [value * -1, key] )
        for k in range(k):
            answer.append(heapq.heappop(heap)[1])
        return answer