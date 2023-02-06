class Solution:
    def racecar(self, target: int) -> int:
        #       position, speed, instruction
        que = deque([(0, 1, 0)])
        visited = set()
        
        while que:
            position, speed, ins = que.popleft()
            pos1, pos2 = position, speed+position
            speed1, speed2 = -1 if speed >= 1 else 1, speed*2
            if pos1 == target or pos2 == target:
                return ins+1
            if pos1 >= 0 and (pos1, speed1) not in visited:
                visited.add((pos1, speed1))
                que.append((pos1, speed1, ins+1))
            
            if pos2 >= 0 and (pos2, speed2) not in visited:
                visited.add((pos2, speed2))
                que.append((pos2, speed2, ins+1))
        return -1