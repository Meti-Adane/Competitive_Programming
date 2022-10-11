class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        nums = [1]
        
        while len(nums) < n:
            newnum = nums[-1] * 10
            while newnum > n:
                newnum //= 10 
                newnum += 1
                while newnum % 10 == 0: 
                    newnum //= 10
                
            nums.append(newnum)
        return nums
        
        
                