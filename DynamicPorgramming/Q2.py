"""
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,
F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.
"""


class Solution:

    # def __init__(self):
    #     self.cache = {}
    #
    def fib(self, n: int):
    #
    #     '''
    #     :param n:
    #     :return:
    #     '''
    #
    #     if n == 0:
    #         return 0
    #
    #     if n == 1:
    #         return 1
    #
    #     self.cache[n] = self.fib(n-1) + self.fib(n-2)
    #     return self.cache[n]

    # O(2^n) time | O(n) space.  keep a cache of n.
        #
        # if n == 0:
        #     return 0
        #
        # if n == 1:
        #     return 1
        #
        # return fib(n-1) + fib(n-2)


        # O(n) time | O(1) space

        if n == 0:
            return 0

        if n == 1:
            return 1

        f1 = 0
        f2 = 1

        for i in range(2, n + 1):
            prev_f1 = f2
            f2 = f1 + f2
            f1 = prev_f1

        return f2



