from typing import List

class Solution:
    def bs(self, row, target):
        low, high = 0, len(row) - 1
        while low <= high:
            mid = (low + high) // 2
            if row[mid] == target:
                return True
            elif row[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
        return False

    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        for i in range(len(matrix)):
            if self.bs(matrix[i], target):
                return True
        return False

