class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        evensum = 0 
        ans = []
        for val in nums:
            if val%2 == 0:
                evensum += val
        
        for val, idx in queries:
            if nums[idx] % 2 == 0:
                evensum -= nums[idx]
            newval = nums[idx] + val
            if newval % 2 ==0 :
                evensum += newval
            nums[idx] = newval
            ans.append(evensum)
            
        return ans 