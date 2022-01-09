"""
Alice and Bob take turns playing a game, with Alice starting first.
Initially, there is a number n on the chalkboard. On each player's turn, that player makes a move consisting of:
Choosing any x with 0 < x < n and n % x == 0.
Replacing the number n on the chalkboard with n - x.
Also, if a player cannot make a move, they lose the game.
Return true if and only if Alice wins the game, assuming both players play optimally.
"""


class Solution:
    def divisorGame(self, n: int):

        '''
        :param n:
        :return:
        '''

        #cache = {}

        # Big Oh without the cache.
        # O(  n^n  ) time | O(n) space.
        # With cache, O( n ^ 2 ) time | O(n) space.
        # def _divisorGame( x ):
        #
        #     # if no number on chalkboard, cannot make the next mvoe
        #     if x == 0:
        #
        #         return False
        #
        #     # if the win bool, true/false is already recorded, just refer from the cache.
        #     if x in cache:
        #
        #         return cache[x]
        #
        #     isWin = False
        #     for i in range( 1, x ):
        #
        #         # i is a divisor, check if the second player wins without the i.
        #         if x % i == 0:
        #
        #             isWin = isWin or not _divisorGame( x - i )
        #
        #     cache[x] = isWin
        #     return cache[x]
        #
        # return _divisorGame(n)

        # bottom-up approach

        # O(N^2) time | O(N) space
        
        dp = [ False ] * (n + 1)

        for i in range(n+1):
            for j in range(1, i):
                if ( i % j == 0 ):
                    dp[i] = dp[i] or not dp[i-j]

        return dp[-1]



if __name__ == "__main__":

    sol = Solution()
    assert( sol.divisorGame(0) == False )
    assert( sol.divisorGame(1) == False )
    assert( sol.divisorGame(2) == True )
    assert ( sol.divisorGame(3) == False )

    #       3
    #      /  \
    #      1   2 (*)
    #           IF ALICE LOOSES HERE, alice will win at 3.


