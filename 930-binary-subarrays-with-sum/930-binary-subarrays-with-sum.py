class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        
        hashmap = {0:1} # hashmap to store the number of odd occurrence 
        count = 0 
        runningSum = 0 
        
        for num in nums:
            if num == 1:
                runningSum += 1
            if runningSum - goal in hashmap:
                count += hashmap[runningSum - goal] 
            hashmap[runningSum] = hashmap.get(runningSum, 0) + 1
        return count 
                
            
        