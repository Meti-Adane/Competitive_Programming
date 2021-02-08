# question url: https://leetcode.com/problems/last-stone-weight/

import heapq
class Solution:
    def lastStoneWeight(self, stones) -> int:

        while len(stones) > 1:
            heapq._heapify_max(stones)
            stone_one = heapq._heappop_max(stones)
            stone_two = heapq._heappop_max(stones)
            if stone_one > stone_two:
                heapq.heappush(stones, abs(stone_two - stone_one))
        if stones: return stones.pop()
        return 0