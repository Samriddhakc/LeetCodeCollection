"""
Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n),
ans[i] is the number of 1's in the binary representation of i.
"""


class Solution:
    def countBits(self, n: int):

        '''
        :param n:
        :return:
        '''
        # (n = 0, c = 0),  (n = 1, c = 1), (n = 2, c = 2), (n = 3, c = 2), (n = 4, c = 2),
        # C[n] := C[n/2] + 1; n is odd.
        #         C[n/2];  n is even.
        # c[7] := C[3] + 1 := 3.
        # C[n] := C[n/2]


if __name__ == "__main__":
    sol = Solution()



