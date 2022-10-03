class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        
        hashmap = {0:1} # hashmap to store the number of odd occurrence 
        count = 0 
        oddOccurrence = 0 
        
        for num in nums:
            if num % 2 == 1:
                oddOccurrence += 1
            if oddOccurrence - goal in hashmap:
                count += hashmap[oddOccurrence - goal] 
            hashmap[oddOccurrence] = hashmap.get(oddOccurrence, 0) + 1
        return count 
                
            
        