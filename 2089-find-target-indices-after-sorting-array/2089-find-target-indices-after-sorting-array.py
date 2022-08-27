class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        count = 0 
        index = 0 
        
        for num in nums:
            if num < target:
                index += 1
            if num == target:
                count += 1
        return [i for i in range(index, index+count)]