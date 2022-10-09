class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        n, m = len(board), len(board[0])
        def isValid(row, col, visited, initial):
            if ( row < 0 or row >= n or 
                 col < 0 or col >= m or 
                 (row, col) in visited or 
                 board[row][col] != initial
                ):
                return False
            return True
        
        def updateBoard(row, col, visited, status, initial):
            if not isValid(row, col, visited, initial):
                return 
            visited.add((row, col))
            board[row][col] = status
            for x, y in directions:
                updateBoard(row+x, col+y, visited, status, initial)
        
        
        for row in range(n):
            for col in range(m):
                if (row == 0 or row >= n-1 or col == 0 or col >= m-1): 
                    updateBoard(row, col, set(), 'P', 'O')
        
        for row in range(1, n-1):
            for col in range(1, m-1):
                updateBoard(row, col, set(), 'X', 'O')
                    
        for row in range(n): #reverse to treat false postives
            for col in range(m):
                if (row == 0 or row >= n-1 or col == 0 or col >= m-1): 
                    updateBoard(row, col, set(), 'O', 'P')