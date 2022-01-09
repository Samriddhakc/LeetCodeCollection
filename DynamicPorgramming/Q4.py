"""
Given an integer numRows, return the first numRows of Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it as shown
"""


class Solution:

    def __init__(self):
        self.cache = {}

    def generteRow( self, i, j ):


        if i == 2 and j <= 1:
            return 1

        if (i, j) in self.cache:
            return self.cache[(i, j)]

        if j <= 0 or j >= ( i - 1 ):
            self.cache[(i, j)] = self.generteRow( i - 1, j - 1 )
            return self.cache[(i, j)]

        self.cache[(i, j)] = self.generteRow( i - 1, j - 1 ) + self.generteRow( i - 1, j )
        return self.cache[(i, j)]

    def generate(self, numRows: int):
        '''
        :param numRows:
        :return:
        '''
        # [1,1]
        #
        # recursion:  F[i][j] := | F[i-1][j-1] + F[i][j-1]  (numRows - 1) > i > 0, (numRows - 1)  > j > 0
        #                        | F[i][j-1]         if i =0 or ncol - 1
        #                        |

        if numRows == 1:
            return [ [1] ]

        if numRows == 2:
            return [ [1], [1, 1] ]

        ans = [ [1], [ 1, 1] ]
        for n_row in range(3, numRows + 1):
            c_row = []                          # O ( numRows *  numRows ) time | O(numRows + numRows - 1 + numRows - 2 ) = O(numRows^2) space.
            for y in range(n_row):
                c_row.append( self.generteRow(  n_row, y ) )
            ans.append(c_row)
        return ans


if __name__ == "__main__":
    sol = Solution()
    print(sol.generteRow(4,0))
    # assert( sol.generate(1) == [[1]] )
    # assert ( sol.generate(2) == [ [1], [1, 1] ] )
    # assert ( sol.generate(3) == [ [1], [1,1], [1, 2, 1] ] )
    print(sol.generate(4))
    assert ( sol.generate(4) ==  [ [1], [1,1], [1, 2, 1], [1, 3, 3, 1] ]  )

