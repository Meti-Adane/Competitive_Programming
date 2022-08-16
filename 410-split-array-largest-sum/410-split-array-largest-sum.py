class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        minSum = max(nums)
        maxSum = sum(nums)
        ans = 0
        while minSum <= maxSum:
            mid = minSum + ((maxSum-minSum) // 2)
            
            if self.canBeSplitted(mid, nums, m):
                ans = mid
                maxSum = mid - 1
            else:
                minSum = mid + 1
        return ans
                
        
    def canBeSplitted(self, target, nums, m):
        numberOfSubarray = 0
        currentSum = 0
        
        for num in nums:
            if num + currentSum > target:
                numberOfSubarray += 1 #start a new sub array
                currentSum = num 
            else:
                currentSum += num
                
        return numberOfSubarray + 1 <= m;
        
        

        