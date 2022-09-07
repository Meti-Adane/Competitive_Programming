class Solution:
    def longestPath(self, arr: List[int], s: str) -> int:
        graph = defaultdict(list)
        visited = [False for _ in range(len(arr))]
        
        for i, parent in enumerate(arr):
            graph[parent].append(i)
            
        self.longest = 1 
        
        
        def dfs(node, lastchar):
            if s[node] == lastchar:
                return 0
            visited[node] = True
            max1, max2, count = 0, 0, 1
            for child in graph[node]:
                ans = dfs(child, s[node]) 
                count = max(ans+1, count)
                if ans > 0:
                    if ans > max2:
                        max1, max2 = max2, ans
                    elif ans > max1:
                        max1 = ans
            self.longest = max(self.longest, (1+max1+max2))
            
            return count
        
        for i in range(len(arr)):
            if not visited[i]:
                dfs(i, "")
        return self.longest