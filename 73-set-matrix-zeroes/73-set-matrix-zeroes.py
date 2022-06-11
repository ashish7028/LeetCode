class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        
        """
        n, m = len(matrix), len(matrix[0])
        rows, cols = {}, {}
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    rows[i] = 1
                    cols[j] = 1
        for i in range(n):
            for j in range(m):
                if i in rows:
                    matrix[i][j] = 0
                if j in cols:
                    matrix[i][j] = 0
        return matrix
        
        """for i in range(len(matrix)):
            for j in range(len(matrix)):
                if matrix[i][j] ==0:
                    for k in range(len(matrix)):
                        matrix[i][k] = 0
                        matrix[k][j] = 0"""
                        
        