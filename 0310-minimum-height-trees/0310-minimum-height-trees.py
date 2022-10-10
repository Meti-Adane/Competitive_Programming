#10:40
class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 2 :
            return [i for i in range(n)]
        
        graph = dict()
        for src, dst in edges:
            if src not in graph:
                graph[src] = set()
            if dst not in graph :
                graph[dst] = set()
            graph[dst].add(src)
            graph[src].add(dst)
            
        leafnodes = []
        for node in graph:
            if len(graph[node]) == 1:
                leafnodes.append(node)
        while n > 2:
            n -= len(leafnodes)
            newleaves=[]
            for leaf in leafnodes:
                neighbor = graph[leaf].pop()
                graph[neighbor].remove(leaf)
                if len(graph[neighbor]) == 1:
                    newleaves.append(neighbor)
            leafnodes = newleaves
        return leafnodes
            
        
                
        
        