"""
Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
"""


class Solution:
    def getRow(self, rowIndex: int):

        '''
        :param rowIndex:
        :return:
        '''

        if rowIndex == 0:
            return [1]

        if rowIndex == 1:
            return [1, 1]

        prev = [1, 1]

        # 1.....row_index sum = O(n(n+1)/2)= O(n^2) time | O(n) space.

        for i in range(2, rowIndex + 1):
            ans = [1]
            for r_idx in range(i - 1):
                ans.append(prev[r_idx] + prev[r_idx + 1])
            ans.append(1)
            prev = ans
        return prev


if __name__ == "__main__":
    sol = Solution()
    assert ( sol.getRow(2) == [1, 2, 1] )
    assert ( sol.getRow(3) == [1, 3, 3, 1] )







