class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        graph = defaultdict(list)
        
        for i in range(10):
            c1 = i + k 
            c2 = i - k 
            
            if c1 < 10:
                graph[str(i)].append(str(c1))
            if c2 >= 0:
                graph[str(i)].append(str(c2))
        
                
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
            dfs([str(i)], graph, ans, n)
        return ans  
                