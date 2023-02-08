class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = dict()
        ans = []
        for i in range(len(equations)):
            a, b = equations[i]
            if a not in graph:
                graph[a] = dict()
            if b not in graph:
                graph[b] = dict()
            graph[b][a] = 1 / values[i]
            graph[a][b] = values[i]
        
        
        def dfs(a, target, runningRatio, visited):
            nonlocal ratio
            if target not in graph or a not in graph or a in visited:
                return False
            if a == target:
                ratio = runningRatio
                return True
            visited.add(a)
            for b, val in graph[a].items(): # dividend : value
                if dfs(b, target, runningRatio * val, visited):
                    return True
            return False
        
        for a, b in queries:
            ratio = -1
            dfs(a, b, 1, set())
            ans.append(ratio)
        return ans 