class Solution:
    def numBusesToDestination(self, routes: List[List[int]], source: int, target: int) -> int:
        graph = defaultdict(list)
        que = deque()
        que.append([source,0])
        visited = set()

        for i, route in enumerate(routes):
            for r in route:
                graph[r].append(i)
            
        while que:
            curr, busesTaken = que.popleft()
            
            if curr == target:
                return busesTaken
            
            for bus in graph[curr]:
                if bus in visited: continue 
                visited.add(bus)
                for nextBus in routes[bus]:
                    que.append([nextBus, busesTaken+1])
        
        return -1