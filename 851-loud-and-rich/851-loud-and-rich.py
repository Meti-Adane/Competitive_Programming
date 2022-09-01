class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        graph = defaultdict(set)
        visited = [False for _ in range(len(quiet))]
        ans = []
        
        
        for person1, person2 in richer:
            graph[person2].add(person1)
         
        def compress(n):
            if visited[n]:
                return 
            visited[n] =True
            riches = set()
            for person in graph[n]:
                
                compress(person)
                riches.update(graph[person])
                
            graph[n].update(riches)
            
        for i in range(len(quiet)):
            compress(i)
            leastquiet, quiteness = i, quiet[i]
            for richerPerson in graph[i]:
                if quiet[richerPerson] <= quiteness:
                    leastquiet, quiteness = richerPerson, quiet[richerPerson] 
            ans.append(leastquiet)
        
        return ans