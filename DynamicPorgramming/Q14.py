class Solution:
    def countVowelStrings(self, n: int) -> int:

        vowels = ["a", "e", "i", "o", "u"]

        dp = [[0 for j in range(6)] for i in range(n + 1)]  # idx * length, dp represents number of vowel strings.

        # dp[idx][l] = sum(dp[i][l-1]) for all comb ending in i and length l. and i = 0,.... idx  ( n * n_vowels )
        # dp[idx][0] = 0
        # dp[0][idx] = idx + 1

        #         *  0  1  2
        #         a  |  1  1
        #         e  |  2  3
        #         i  |  3  6
        #         o  |  4  10
        #         u  |  5  15

        # dp[n][v] = dp[n-1][v] + dp[n][v-1]
        # dp[n][1] = 1
        # dp[1][v] = v

        #         *  0  1  2
        #         a  |  1  1
        #         e  |  2  3
        #         i  |  3  6
        #         o  |  4  10
        #         u  |  5  15

        for x in range(1, n + 1):
            dp[x][1] = 1

        for v in range(1, 6):
            dp[1][v] = v

        for x in range(2, n + 1):
            for v in range(1, 6):
                dp[x][v] = dp[x - 1][v] + dp[x][v - 1]

        return dp[-1][-1]

#         def _countVowels( start_idx, x ):

# #             if start_idx == len(vowels):

# #                   return 0

#             if x == 0:

#                 return 1

#             if dp[start_idx][x]:

#                 return dp[start_idx][x]


#             total_strings = 0

#             for idx in range(start_idx, len(vowels)):

#                 total_strings += _countVowels( idx, x - 1 )

#             dp[start_idx][x] = total_strings
#             return total_strings

#         return _countVowels( 0, n )


#               ( 0, 2 )
#               /      \
#             ( 0, 1 ) ( 1, 1 )
#              / \          /  \
#            ()  ( 1, 0 ) (0, 0) (1, 0)

# sum ( x ^ n ) x = 1, 5. O( 5 ^ n )
#
#
#