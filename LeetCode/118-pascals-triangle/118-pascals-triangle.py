class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        arr = [[1]]
        for i in range(1, numRows):
            arr.append([1] + [arr[i-1][j] + arr[i-1][j+1] for j in range(len(arr[i-1]) - 1)] + [1])
        return arr