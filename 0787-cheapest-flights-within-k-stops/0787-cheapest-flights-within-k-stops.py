class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, destination: int, k: int) -> int:
        heap = [(0, 0, src)]
        hashmap = defaultdict(list)
        visited = set()

        for src, dst, cost in flights:
            hashmap[src].append((dst, cost))

        while heap:
            price, stops, node = heapq.heappop(heap)
            if node == destination:
                return price
            if stops > k or (node, stops) in visited: continue
            visited.add((node, stops)) 
            for nextDst, cost in hashmap[node]:
                heapq.heappush(heap, (price+cost, stops+1, nextDst))

        return -1
