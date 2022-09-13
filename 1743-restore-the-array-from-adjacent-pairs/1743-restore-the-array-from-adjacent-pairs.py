class Solution:
    def restoreArray(self, adjacentPairs: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        ans = []
        start = -1
        visited = set()
        
        for u, v in adjacentPairs:
            graph[u].append(v)
            graph[v].append(u)
          
        for key, val in graph.items():
            if len(val) == 1:
                start = key
                break
        
        def builder(node, visited):
            nonlocal ans
            ans.append(node)
            visited.add(node)
            for c in graph[node]:
                if c not in visited:
                    builder(c, visited)
        builder(start, visited)
        return ans
    
        