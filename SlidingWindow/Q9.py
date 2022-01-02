"""
Q9.2107. Number of Unique Flavors After Sharing K Candies
You are given a 0-indexed integer array candies, where candies[i] represents the flavor of the ith candy. Your mom wants you to share these candies with your little sister by giving her k consecutive candies, but you want to keep as many flavors of candies as possible.

Return the maximum number of unique flavors of candy you can keep after sharing with your sister.
"""

from collections import Counter
class Solution:

    def shareCandies(self, candies, k):

        '''
        :param candies:
        :param k:
        :return:
        '''

        # Find the max number of unique numbers in a k window.
        k_unique_max = len(set(candies[:k]))
        hash_count = Counter(candies)

        for up_idx in range( k, len(candies) ):
            left_el = candies[up_idx - k]
            hash_count[left_el] -= 1
            if hash_count[left_el] == 0:
                hash_count.pop(left_el)
            hash_count[candies[up_idx]] += 1
            k_unique_max = max( k_unique_max, len(hash_count) )

        return k_unique_max



if __name__ == "__main__":
    sol = Solution()
    print( sol.shareCandies( [1,2,2,3,3,3],  2) )

