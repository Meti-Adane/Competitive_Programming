class Solution:
    def maxLength(self, arr: List[str]) -> int:
        que = deque()
        i, ans = len(arr)-1 ,0
        
        while i >= 0:
            if len(arr[i]) != len(set(arr[i])):
                i -= 1
                continue 
            ans = max(ans, len(arr[i]))
            for j in range(1, len(que)+1):
                l1, l2 = len(arr[i]), len(que[-j])
                combined = set(arr[i]) | set(que[-j])
                
                if len(combined) == l1+l2:
                    ans = max(ans, l1+l2)
                    que.appendleft(arr[i]+que[-j])
                    
            que.appendleft(arr[i])
            i -= 1
        return ans 
                    
                
        