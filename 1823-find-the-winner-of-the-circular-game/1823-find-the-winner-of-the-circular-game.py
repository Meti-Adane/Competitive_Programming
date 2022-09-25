class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        arr = [1 for _ in range(n)]
        players = set(i+1 for i in range(n))
        i = 0
        stop = k
        while len(players) > 1:
            if i >= n:
                i = 0
            if not arr[i]:
                i += 1
                continue
            stop -= 1
            if stop == 0:
                arr[i] = 0
                players.remove(i+1)
                stop = k
                
            
            i += 1
                
       
        return players.pop()