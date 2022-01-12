'''
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.
A subsequence of a string is a new string that is formed from the original string by deleting some (can be none)
of the characters without disturbing the relative positions of the remaining characters.
(i.e., "ace" is a subsequence of "abcde" while "aec" is not).
'''


class Solution:
    def isSubsequence(self, s: str, t: str):

        '''
        :param s:
        :param t:
        :return:
        '''
        if len(s) > len(t):
            return False

            # bac   dabc
            # |     |
            # p1, p2 = 0, 0
            # if p2 == len(s) -> return False, if p1 == len(s): return True
            # if s[p1] == s[p2]: p1 += 1, p2 += 1
            # if s[p1] != s[p2]: resuvisively call (p1 + 1, p2), (p1, p2 + 1)
            #
            # cache = {}

            # take care of empty strings case.

            #         p1 = 0
            #         for p2 in range(len(t)):
            #             if s and s[p1] == t[p2]:
            #                 p1 += 1

            #             if p1 == len(s):
            #                 return True

            #         return True if p1 == len(s) else False

            # dp using levensthien distance

        if len(s) == 0:
            return True

        dp = [[0 for i in range(len(t) + 1)] for j in range(len(s) + 1)]

        # levenstien distance.
        # Big O ( Olen(s) * len(t) ) time | O ( len(s) * len(t) ) space
        for row in range(1, len(s) + 1):
            for col in range(1, len(t) + 1):
                if t[col - 1] == s[row - 1]:
                    dp[row][col] = 1 + dp[row - 1][col - 1]
                else:
                    dp[row][col] = max(dp[row][col - 1], dp[row - 1][col])
            if dp[len(s)][col] == len(s):
                return True

        print(dp)
        return False



