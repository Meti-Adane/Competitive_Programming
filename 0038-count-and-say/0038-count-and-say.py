class Solution:
    def countAndSay(self, n: int) -> str:
        ans = ["1"]
        for _ in range(1,n):
            newans = [] 
            i = 0 
            while i < len(ans):
                prev = j = i
                count = 0 
                while j < len(ans) and ans[j] == ans[prev]:
                    j += 1
                    count += 1
                newans.append(str(count))
                newans.append(ans[prev])
                i = j 
            ans = newans.copy()
            
        return "".join(ans)
                

        