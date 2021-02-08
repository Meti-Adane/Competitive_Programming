# question url : https://leetcode.com/problems/top-k-frequent-words/
import collections
import heapq

class Solution:
    def topKFrequent(self, words: [str], k: int) -> [str]:
        count_dict  = dict(collections.Counter(words))
        heap=[]
        ans =[]
        for key, value in count_dict.items():
            heapq.heappush(heap, [value * -1, key])
        for k in range(k):
            ans.append(heapq.heappop(heap)[1])
        return ans