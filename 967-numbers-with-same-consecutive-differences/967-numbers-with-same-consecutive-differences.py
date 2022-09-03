class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        graph = defaultdict(list)
        digit = {
            0:"0",
            1:"1", 
            2:"2", 
            3:"3", 
            4:"4",
            5:"5", 
            6:"6",
            7:"7",
            8:"8",
            9:"9"
        }
        for i in range(10):
            c1 = i + k 
            c2 = i - k 
            
            if c1 < 10:
                graph[digit[i]].append(digit[c1])
            if c2 >= 0:
                graph[digit[i]].append(digit[c2])
        
                
        def dfs(arr, graph, ans, n):
            if len(arr) == n:
                return ans.add("".join(arr.copy()))
            
            last = arr[-1]
            for num in graph[last]:
                arr.append(num)
                dfs(arr, graph, ans, n)
                arr.pop()
            return
        
        ans = set()
        for i in range(1, 10):
            dfs([digit[i]], graph, ans, n)
        return ans  
                