
class Solution:

    def maxProfit(self, prices):

        # Brute force solution O(N^2) time | O(1) space.
        # max_profit = 0
        # for i in range(len(prices)):
        #     for j in range( i + 1, len(prices)):
        #         max_profit = max( max_profit, prices[j] - prices[i] )
        #
        #
        # return max_profit

        # O(N) time | O(1) space

        if not prices:

            return 0

        min_val, max_profit = prices[0], 0

        for p_idx in range(  1, len(prices) ):

            max_profit = max ( max_profit, prices[p_idx] - min_val )
            min_val = min ( min_val, prices[p_idx] )

        return max_profit

if __name__ == "__main__":

    sol = Solution()
    assert( sol.maxProfit( [] ) == 0  )
    assert ( sol.maxProfit( [1, 0, 2, 3 ] ) == 3 )
    assert ( sol.maxProfit( [100, 120, 150 ] ) == 50 )
    assert ( sol.maxProfit([150, 149, 0]) == 0 )
