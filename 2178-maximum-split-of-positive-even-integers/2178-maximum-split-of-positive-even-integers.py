class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        if finalSum % 2 == 1:
            return []
        ans = []
        n = 2
        
        while finalSum >= n:
            if finalSum - n <= n:
                ans.append(finalSum)
                break
            ans.append(n)
            finalSum -= n
            n += 2
            
        return ans