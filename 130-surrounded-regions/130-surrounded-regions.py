class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        n, m = len(board), len(board[0])
        visited = set()
        
        def isValid(row, col, visited, initial):
            return  not (row < 0 or row >= n or col < 0 or col >= m or 
                         (row, col) in visited or board[row][col] != initial)
        
        def caputureUnsurounded(row, col, visited, initial):
            if not isValid(row, col, visited, initial):
                return 
            visited.add((row, col))
            for x, y in directions:
                caputureUnsurounded(row+x, col+y, visited, initial)
        
        
        for row in range(n):
            for col in range(m):
                if (row == 0 or row >= n-1 or col == 0 or col >= m-1): 
                    caputureUnsurounded(row, col, visited,'O')

        for row in range(n): #update every cell with 0 to x if not in unsurounded region
            for col in range(m):
                if (row, col) not in visited and board[row][col] == 'O':
                    board[row][col]  = 'X'