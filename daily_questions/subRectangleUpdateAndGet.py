# question url : https://leetcode.com/problems/subrectangle-queries/


class SubrectangleQueries:

    def __init__(self, rectangle):
        self.list = rectangle
        self.visited = set()

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:

    # ************ Method 1: DFS *********************
        if (row1,col1) in self.visited and self.list[row1][col1] == newValue:
            return
        self.list[row1][col1] = newValue
        self.visited.add((row1, col1))
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        for direction in directions:
            newRow = row1 + direction[0]
            newCol = col1 + direction[1]
            if newRow >= row1 and newRow <= row2 and newCol >= col1 and newCol <= col2:
                self.updateSubrectangle(newRow, newCol, row2, col2, newValue)

    # ************** Method 2: using for loops easier and faster *************
    #     for row in range(row1, row2 + 1):
    #         for col in range(col1, col2 + 1):
    #             self.list[row][col] = newValue


    def getValue(self, row: int, col: int) -> int:
        return self.list[row][col]
