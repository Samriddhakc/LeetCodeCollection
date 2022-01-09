"""
Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n),
ans[i] is the number of 1's in the binary representation of i.
"""


class Solution:


    # def numOnes(self, x, cache):
    #
    #     '''
    #     :param x:
    #     :return:
    #     '''
    #     # Big O. O(lgx) time | O(lgx) space
    #
    #     if x == 0:
    #         return 0
    #
    #     if x in cache:
    #         return cache[x]
    #
    #     cache[x] = ( self.numOnes(x//2, cache) + x % 2 )
    #     return cache[x]

    def countBits(self, n: int):

        '''
        :param n:
        :return:
        '''
        # (n = 0, c = 0),  (n = 1, c = 1), (n = 2, c = 2), (n = 3, c = 2), (n = 4, c = 3),
        # C[n] := C[n//2] + 1
        # Big O, O(n) time | O(n) space.
        # cache = {}
        # ans = [] # O(n * sum(xlgx) ) time | O(1) extra space.
        # for i in range(n+1):
        #     ans.append( self.numOnes(i, cache) )
        #
        # return ans

        # optimize further by doing a bottom up dp
        dp = [ 0 ]

        for i in range(1, n+1):
            dp.append( dp[i//2] + i % 2 )
        return dp

if __name__ == "__main__":
    sol = Solution()
    print(sol.countBits(1))
    assert( sol.countBits(1) == [0,1] )
    assert( sol.countBits(2) == [0, 1, 1] )
    assert (sol.countBits(3) == [0, 1, 1, 2] )
    assert ( sol.countBits(4) == [0, 1, 1, 2, 1] )
    assert ( sol.countBits(7) == [0, 1, 1, 2, 1, 2, 2, 3] )
    assert ( sol.countBits(8) ==  [0, 1, 1, 2, 1, 2, 2, 3, 1] )



