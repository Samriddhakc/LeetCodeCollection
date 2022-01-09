"""
The Tribonacci sequence Tn is defined as follows:
T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.
Given n, return the value of Tn.
"""


class Solution:
    def tribonacci(self, n: int):

        '''
        :param n:
        :return:
        '''
        if n == 0:
            return 0

        if n <= 2:
            return 1

        f1 = 0
        f2 = 1
        f3 = 1

        for i in range(3, n + 1):
            f3 = f2 + f1
            f1  = f2
            f2 =  f3

        return f3