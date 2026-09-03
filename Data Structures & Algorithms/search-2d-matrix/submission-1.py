class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        l, r = 0, len(matrix) - 1
        if matrix[l][0] > target:
            return False
        elif matrix[r][0] <= target:
            l = r
        while r - l > 1:
            mid = (r + l) // 2
            if matrix[mid][0] <= target:
                l = mid
            else:
                r = mid
        row = l
        l, r = 0, len(matrix[row]) - 1
        if matrix[row][l] >= target:
            r = l
        while r - l > 1:
            mid = (r + l) // 2
            if matrix[row][mid] < target:
                l = mid
            else:
                r = mid
        return matrix[row][r] == target