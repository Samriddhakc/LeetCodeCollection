"""
Q14. Minimum Swaps to Group all 1's Together.
Given a binary array data, return the minimum number of swaps required to group all 1’s present in the array
together in any place in the array.
"""
# In a window of size num of 1s, find the window the minimum 0s.

class Solution:
    def minSwaps(self, data):

        '''
        :param data:
        :return:
        '''
        wind_size = data.count(1)
        num_zeros = data[:wind_size].count(0)
        min_zeros = num_zeros
        for r in range(wind_size, len(data)):
            num_zeros -= (1 - data[r - wind_size])
            num_zeros += (1 - data[r])
            min_zeros = min ( min_zeros, num_zeros )

        return min_zeros


if __name__ == "__main__":
    sol = Solution()