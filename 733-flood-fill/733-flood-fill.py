class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        target = image[sr][sc]
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        visited = set()
        
        def isValid(row, col):
            if (row < 0 or row >= len(image) or
               col < 0 or col >= len(image[0]) or
                image[row][col] != target or 
                (row, col) in visited
               ):
                return False
            return True
        
        
        def colorImage(row, col):
            visited.add((row, col))
            image[row][col] = color
            for x, y in directions:
                if isValid(row+x, col+y) :
                    colorImage(row+x, col+y)
            return image
        
        return colorImage(sr, sc)
       