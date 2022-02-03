# note.
#
# class Solution:
#     def rotate(self, matrix: List[List[int]]) -> None:
#         n = len(matrix[0])
#         for i in range(n // 2 + n % 2):
#             for j in range(n // 2):
#                 tmp = matrix[n - 1 - j][i]
#                 matrix[n - 1 - j][i] = matrix[n - 1 - i][n - j - 1]
#                 matrix[n - 1 - i][n - j - 1] = matrix[j][n - 1 -i]
#                 matrix[j][n - 1 - i] = matrix[i][j]
#                 matrix[i][j] = tmp


class Solution:
    def rotate(self, matrix):

        # O( N * M ) time | O(max(N,M)) space
        """
        Do not return anything, modify matrix in-place instead.
        """

        ncols, nrows = len(matrix[0]), len(matrix)
        start_row = 0
        start_col = 0

        while start_row < nrows and start_col < ncols:

            prev = matrix[start_row][start_col:ncols - start_col]

            i = 0

            for r in range(start_row, nrows - start_row):
                prev_val = matrix[r][ncols - start_col - 1]
                matrix[r][ncols - start_col - 1] = prev[i]
                prev[i] = prev_val
                i += 1

            if prev:
                nx_val = prev[-1]

            i = 0
            for c in range(ncols - start_col - 1, start_col - 1, -1):

                prev_val = matrix[nrows - start_row - 1][c]
                matrix[nrows - start_row - 1][c] = prev[i]
                if i > 0:
                    prev[i] = prev_val
                i += 1

            if prev:
                prev[0] = nx_val

            i = 0
            if prev:
                nx_val = prev[-1]
            for r in range(nrows - start_row - 1, start_row - 1, -1):

                prev_val = matrix[r][start_col]
                matrix[r][start_col] = prev[i]
                if i > 0:
                    prev[i] = prev_val
                i += 1

            if prev:
                prev[0] = nx_val

            i = 0
            if prev:
                nx_val = prev[-1]

            for c in range(start_col, ncols - start_col):
                prev_val = matrix[start_row][c]
                matrix[start_row][c] = prev[i]
                if i > 0:
                    prev[i] = prev_val
                i += 1

            start_row += 1
            start_col += 1


