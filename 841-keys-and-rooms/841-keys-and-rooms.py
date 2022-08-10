class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        keys = deque()
        keys.append(0)
        visited = set()
        visited.add(0)
        
        while keys:
            roomid = keys.pop()
            for key in rooms[roomid]:
                if key not in visited:
                    visited.add(key)
                    keys.append(key)
        return len(visited) == len(rooms)
                