# Given an m x n matrix, return all elements of the matrix in spiral order.

class Solution:
    def spiralOrder(self, matrix ):

        '''
        :param matrix:
        :return:
        '''

        if not matrix:

            return []

        n, m = len(matrix), len(matrix[0])
        res = []
        u_limit, d_limit, l_limit, r_limit= 1, len(matrix) - 1, 0, len(matrix[0]) - 1
        i, j = 0, 0
        direction = [ (0, 1), (1, 0), (0, -1), (-1, 0) ]
        d = 0
        while len(res) < n * m:

            res.append( matrix[i][j] )

            if j == r_limit and d == 0:
                d = ( d + 1 ) % 4
                r_limit -= 1

            if i == d_limit and d == 1:
                d = (d + 1) % 4
                d_limit -= 1

            if j == l_limit and d == 2:
                d = (d + 1) % 4
                l_limit += 1

            if i == u_limit and d == 3:
                d = (d + 1) % 4
                u_limit += 1

            d_x, d_y = direction[d]
            i += d_x
            j += d_y


        return res