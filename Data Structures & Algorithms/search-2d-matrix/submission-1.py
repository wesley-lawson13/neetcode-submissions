class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        ROWS, COLS = len(matrix), len(matrix[0])
        total = ROWS * COLS

        start, end = 0, total - 1
        while start <= end:

            pos = start + ((end - start) // 2)

            r = pos // COLS
            c = pos % COLS

            if matrix[r][c] == target:
                return True

            if matrix[r][c] > target:
                end = pos - 1
            else:
                start = pos + 1

        return False
