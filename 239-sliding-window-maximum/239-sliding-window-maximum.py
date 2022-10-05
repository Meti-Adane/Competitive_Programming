class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums
        ans, heap = [], []
       
        for i in range(len(nums)-1, len(nums)-k-1, -1):
            heappush(heap, (-1*nums[i], i))
        i = len(nums)-k-1 
        ans.append(-1* heap[0][0])
        
        while i >= 0:
            heappush(heap, (-1*nums[i], i))
            while i < heap[0][1]-k+1:
                heappop(heap)
            ans.append(-1* heap[0][0])
            
            i -= 1
        return ans[::-1] 
        