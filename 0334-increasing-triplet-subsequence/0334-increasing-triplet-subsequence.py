class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        firstsmaller = secondsmaller = float('inf')
        
        for num in nums:
            if num > secondsmaller: #checks if the previous sequence was a valid triplet [5, 7, 2, 9] --> when we get to 2 first smaller gets updated so when we get to nine by placing this check first ene i get to see if there was a previous pair (here preserved by second smaller number) that could be combined with this new num ena give me valid triplet
                return True
            if num <= firstsmaller:
                firstsmaller = num
            elif num < secondsmaller:
                secondsmaller = num
            
        return False