class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        firstsmaller = secondsmaller = float('inf')
        
        for num in nums:
            if num > secondsmaller: 
                return True
            if num <= firstsmaller:
                firstsmaller = num
            elif num < secondsmaller:
                secondsmaller = num
            
        return False