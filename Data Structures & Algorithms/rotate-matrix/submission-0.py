class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # n be n-th Index
        # r, c
        # c, n-r
        # n-r, n-c
        # n-r, c
        n = len(matrix) - 1
        half = len(matrix) // 2
        for r in range(half + (1 if len(matrix) % 2 == 1 else 0)):
            for c in range(half):
                matrix[c][n-r], matrix[n-r][n-c], matrix[n-c][r], matrix[r][c] = matrix[r][c], matrix[c][n-r], matrix[n-r][n-c], matrix[n-c][r]
        
