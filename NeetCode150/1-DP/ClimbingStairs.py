class Solution:

    def __init__(self): 

        self.memo = {}
        
    def climbStairs(self, n: int) -> int:
        
        # def _CountNumToClimbStairs(n): 

        #     if n <= 1: 

        #         return 1 

        #     if n in self.memo: 

        #         return self.memo[n]

        #     self.memo[n] = _CountNumToClimbStairs(n-1) + _CountNumToClimbStairs(n-2)
        #     return self.memo[n]

        dp = [0 for i in range(n+1)] # num ways to climb sairs
       
        dp[0], dp[1] = 1, 1

        for j in range(2, n + 1): 

            dp[j] = dp[j-1] + dp[j-2]
        
        return dp[-1]
    