class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        
        def bfs(coins, amount):
            que = deque([(0, 0)])
            visited = set()
            while que:
                runningSum, length = que.popleft()
                for coin in coins:
                    if runningSum + coin == amount:
                        return length+1 
                    if runningSum + coin not in visited and runningSum + coin <= amount:
                        visited.add(runningSum+coin)
                        que.append((runningSum+coin, length+1))
                
            return -1
        
        return 0 if amount == 0 else bfs(coins, amount) 
    
        
        
