class Solution:
    def longestPath(self, arr: List[int], s: str) -> int:
        graph = defaultdict(list)
        
        for i, parent in enumerate(arr):
            graph[parent].append(i)
            
        self.longest = 1 
        
        
        def dfs(node):
            max1, max2, count = 0, 0, 1
            for child in graph[node]:
                ans = dfs(child) 
                if s[child] != s[node]:
                    count = max(ans+1, count)
                    if ans > max2:
                        max1, max2 = max2, ans
                    elif ans > max1:
                        max1 = ans
            self.longest = max(self.longest, (1+max1+max2))
            
            return count
        
        
        dfs(0)
        return self.longest