class Solution:

    def __init__(self): 

        self.memo = {}

    def minCostClimbingStairs(self, cost: List[int]) -> int:

        num_stairs = len(cost)

        dp = [0 for j in range(num_stairs)]
        # cost.append(0)

        dp[0], dp[1] = cost[0], cost[1]

        for idx in range(2, num_stairs):

            dp[idx] = cost[idx] + min(dp[idx - 1], dp[idx - 2])

        return min(dp[num_stairs - 1], dp[num_stairs - 2])

        # def _minCostClimbingStairs(cost, stair_idx): 

        #     if stair_idx >= num_stairs: 

        #         return 0 

        #     if stair_idx in self.memo: 

        #         return self.memo[stair_idx]

        #     curr_cost = cost[stair_idx] + min(_minCostClimbingStairs(cost, stair_idx + 1),_minCostClimbingStairs(cost, stair_idx + 2))

        #     self.memo[stair_idx] = curr_cost 

        #     return self.memo[stair_idx]

        # return min(_minCostClimbingStairs(cost, 0), _minCostClimbingStairs(cost, 1))


            
        