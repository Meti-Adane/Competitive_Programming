class Solution:
    def matrixBlockSum(self, mat: List[List[int]], k: int) -> List[List[int]]:
        prefixSum = copy.deepcopy(mat)
        n, m, p = len(mat), len(mat[0]), k+1
        ans = [[0 for _ in range(m)] for _ in range(n)]

        for i in range(n):
            for j in range(m):
                prefixSum[i][j] += 0 if i-1 < 0 else prefixSum[i-1][j]
                prefixSum[i][j] += 0 if j -1 < 0 else prefixSum[i][j-1]
                prefixSum[i][j] -= prefixSum[i-1][j-1] if (i-1 >= 0 and j -1 >= 0) else 0 
        
        for i in range(n):
            for j in range(m):
                row, col = min(n-1, i+k), min(m-1, j+k)
                removedCol = 0 if j-p < 0 else prefixSum[row][j-p]
                removedRow = 0 if i-p < 0 else prefixSum[i-p][col]
                commonCell = 0 if (i-p < 0 or j-p < 0) else prefixSum[i-p][j-p]
                ans[i][j] =  prefixSum[row][col] - removedCol - removedRow + commonCell
        return ans
        