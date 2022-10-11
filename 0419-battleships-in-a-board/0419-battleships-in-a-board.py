class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        n, m = len(board), len(board[0])
        count = 0
        
        
        for i in range(n):
            for j in range(m):
                if board[i][j] == 'X' and (j == m-1 or board[i][j+1]=='.') and (i == n-1 or board[i+1][j] == '.'):
                    count += 1
        return count 
                    