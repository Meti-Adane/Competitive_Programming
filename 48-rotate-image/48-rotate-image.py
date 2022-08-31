class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n, m = len(matrix), len(matrix[0])
        left, right, top , bottom = 0, m-1, 0, n-1
        
        
        while left < right and top < bottom :
            arr = []
            # update right most cells 
            for i in range(left+1, right+1):
                arr.append(matrix[top][i])
            matrix[top][right] = matrix[top][left]
            j = 0 
            for i in range(top+1, bottom+1):
                temp = matrix[i][right] 
                matrix[i][right] = arr[j]
                arr[j] = temp
                j += 1
            right -= 1
            # update bottom cells
            j = 0
            for i in range(right, left-1, -1):
                temp = matrix[bottom][i]
                matrix[bottom][i] = arr[j]
                arr[j] = temp
                j += 1
            bottom -= 1
            j = 0
            for i in range(bottom, top-1, -1):
                temp = matrix[i][left]
                matrix[i][left] = arr[j]
                arr[j] = temp
                j += 1
            left += 1
            j = 0 
            for i in range(left, right+1):
                temp = matrix[top][i]
                matrix[top][i] = arr[j]
                j += 1
            top += 1