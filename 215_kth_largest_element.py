class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = []
        for num in nums:
            heappush(heap, -1 * num)
            
        while k -1 and heap:
            heappop(heap)
            k -= 1
        return -1 * heappop(heap)