class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        pos, deg = [0, 0], 0
        direction = [(0, 1), (1, 0), (0, -1), (-1,0)]
        for char in instructions:
            if char == 'R':
                deg = (deg +1) % 4 
            elif char == 'L':
                deg = (deg -1) % 4
            else:
                pos[0] += direction[deg][0]
                pos[1] += direction[deg][1]
        return deg != 0 or pos == [0, 0]