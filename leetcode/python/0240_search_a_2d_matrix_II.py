class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        return self.binarySearchConstantSpace(matrix, target)

    def binarySearchConstantSpace(self, matrix, target):
        row, col = len(matrix) - 1, 0
        while row < len(matrix) and row >= 0 and col < len(matrix[0]) and col >= 0:
            middle = matrix[row][col]

            if middle == target: return True
            elif middle < target: col += 1
            else: row -= 1
        
        return False