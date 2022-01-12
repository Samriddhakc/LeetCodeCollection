class Solution:
    def climbStairs(self, n ):
        '''

        :param n:
        :return:
        '''

        if n < 0:
            return 0

        if n == 0:
            return 1

        f2 = 0
        f1 = 1

        for idx in range(1, n + 1):
            prev_f1 = f1
            f1 = f2 + f1
            f2 = prev_f1

        return f1

    #         if n < 0:

    #             return 0

    #         if n == 0:

    #             return 1

    #         if n in self.cache:

    #             return self.cache[n]

    #         self.cache[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
    #         return  self.cache[n]
