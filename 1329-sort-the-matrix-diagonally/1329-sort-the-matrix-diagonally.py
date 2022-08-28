class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        diag_values = dict()
        visited = set()
        
        def isValid(i, j):
            if ( i < 0 or i >= len(mat) or j < 0 or j >= len(mat[0]) or (i, j) in visited): return False
            return True
        
        def populate(i, j):
            cell = (i, j)
            diag_values[cell] = []
            
            while isValid(i, j):
                visited.add((i, j))
                heappush(diag_values[cell], mat[i][j])
                i += 1
                j += 1
        
        def sortdiag(i, j):
            cell = (i, j)
            while diag_values[cell] != None and isValid(i, j):
                visited.add((i, j))
                mat[i][j] = heappop(diag_values[cell])
                i += 1
                j += 1
            
        
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if (i, j) not in visited:
                    populate(i, j)
        
        visited.clear()
        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if (i, j) not in visited:
                    sortdiag(i, j)
        return mat