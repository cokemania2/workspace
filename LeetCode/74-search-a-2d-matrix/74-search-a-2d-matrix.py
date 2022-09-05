class Solution:
    def binary_search_matrix(self, matrix, target):
        answer, left, right = 0, 0, len(matrix) - 1
        while left <= right:
            mid = (left + right) // 2
            if matrix[mid][-1] >= target and matrix[mid][0] <= target:
                return mid
            elif matrix[mid][-1] < target:
                left = mid + 1
            else:
                right = mid - 1
        return answer
    
    def binary_search(self, arr, target):
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == target:
                return True
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return False
    
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        matrix_index = self.binary_search_matrix(matrix, target)
        print(matrix_index)
        return self.binary_search(matrix[matrix_index], target)