class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if x < arr[0]:
            idx = -1
        if x > arr[-1]:
            idx = len(arr)
        ans = [] 
        heap = []
        for i, num in enumerate((arr)):
            heappush(heap, (abs(num-x), num))
        
        while k and heap:
            ans.append(heappop(heap)[1])
            k -=1 
            
        return sorted(ans)