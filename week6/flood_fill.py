# question url:https://leetcode.com/problems/flood-fill/


class Solution:
    def floodFill(self, image: [[int]], sr: int, sc: int, newColor: int) ->[[int]]:
        removedColor = image[sr][sc]
        image[sr][sc] = newColor
        visited = set()
        rowNo = len(image)
        colNo = len(image[0])

        self.dfs(image, sr, sc, rowNo, colNo, newColor, removedColor, visited)

        return image

    def dfs(self, image, rowIndex, colIndex, rowNo, colNo, newColor, removedColor, visited):
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        for direction in directions:
            nextNodeRow = rowIndex + direction[0]
            nextNodeCol = colIndex + direction[1]
            if 0 <= nextNodeRow < rowNo and 0 <= nextNodeCol < colNo and image[nextNodeRow][
                nextNodeCol] == removedColor:
                print("here")
                nextNode = (nextNodeRow, nextNodeCol)
                if nextNode not in visited:
                    image[nextNodeRow][nextNodeCol] = newColor
                    visited.add(nextNode)
                    self.dfs(image, nextNodeRow, nextNodeCol, rowNo, colNo, newColor, removedColor, visited)