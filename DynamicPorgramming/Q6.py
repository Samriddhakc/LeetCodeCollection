"""
You are given an integer array cost where cost[i] is the cost of ith step on a staircase.
 Once you pay the cost, you can either climb one or two steps.
You can either start from the step with index 0, or the step with index 1.
Return the minimum cost to reach the top of the floor.
"""


class Solution:
    def minCostClimbingStairs( self, cost ):

        '''
        :param cost:
        :return:
        '''

        # O(len(arr)) time | O(len(arr)) space
        # cache = {}
        #
        # def _minCostClimbingStairs(arr, curr_idx):
        #
        #     if curr_idx >= len(cost):
        #         return 0
        #
        #     if curr_idx in cache:
        #         return cache[curr_idx]
        #
        #     cache[curr_idx] = arr[curr_idx] + min(_minCostClimbingStairs(arr, curr_idx + 2),
        #                                           _minCostClimbingStairs(arr, curr_idx + 1))
        #     return cache[curr_idx]
        #
        # return min(_minCostClimbingStairs(cost, 0), _minCostClimbingStairs(cost, 1)) if len(
        #     cost) > 1 else _minCostClimbingStairs(cost, 0)

        # top down approach
        # bottom up approach:
        if len(cost) == 0:
            return 0

        if len(cost) == 1:

            return cost[0]

       # dp = [1, 2, 1, "DEST"]
        dp = [ 0 ] * (len(cost) + 1)
        dp[0] = 0
        dp[1] = cost[0]
        for idx in range(2, len(cost) + 1): #dp cost of stepping on the i^th step.
            dp[idx] =  cost[idx-1]  + min( dp[idx-2], dp[idx-1] )

        return min(dp[-1], dp[-2])

if __name__ == "__main__":
    sol = Solution()
    # assert( sol.minCostClimbingStairs([]) == 0 )
    # assert( sol.minCostClimbingStairs([1]) == 1 )
    # assert( sol.minCostClimbingStairs([1, 2]) == 1 )
    assert( sol.minCostClimbingStairs([1, 2, 1]) == 2 ) # dp = [0, 1, 1, ]



