# Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's, and return the matrix.
#
# You must do it in place.
#
# #


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:

        """
        Do not return anything, modify matrix in-place instead.
        """
        is_first_col = False
        for row in range(len(matrix)):
            if matrix[row][0] == 0:
                is_first_col = True
            for col in range(1, len(matrix[0])):
                if matrix[row][col] == 0:
                    if col == 0:
                        is_first_col = True
                    matrix[row][0] = 0
                    matrix[0][col] = 0

        for row in range(1, len(matrix)):
            for col in range(1, len(matrix[0])):
                if not matrix[row][0] or not matrix[0][col]:
                    matrix[row][col] = 0

                    # accross first
        if matrix[0][0] == 0:

            for r in range(len(matrix[0])):
                matrix[0][r] = 0

        if is_first_col:

            for c in range(len(matrix)):
                matrix[c][0] = 0

        return matrix

    #         c = set()
#         column_zeros = set()
#         row_zeros = set()

#         for row in range(len(matrix)):
#             for col in range(len(matrix[0])):
#                 if matrix[row][col] == 0:
#                     row_zeros.add(row)
#                     column_zeros.add(col)


#         for row in range(len(matrix)):
#             for col in range(len(matrix[0])):
#                 if row in row_zeros or col in column_zeros:
#                     matrix[row][col] = 0

#         return matrix






