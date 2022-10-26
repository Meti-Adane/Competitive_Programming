class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        hashmap = {0:-1}
        runningSum = 0 
        
        for i, num in enumerate(nums):
            runningSum += num 
            rem = runningSum % k 
            if rem in hashmap and (i - hashmap[rem]) >= 2:
                return True 
            if rem not in hashmap:
                hashmap[rem] = i
        return False 
        