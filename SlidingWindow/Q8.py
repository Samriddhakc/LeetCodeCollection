"""
Q8. Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold
Given an array of integers arr and two integers k and threshold, return the number of sub-arrays of size k
and average greater than or equal to threshold.
"""

class Solution:

    def numOfSubarrays(self, arr, k, threshold):

        '''
        :param arr:
        :param k:
        :param threshold:
        :return:
        '''

        k_running_sum = sum(arr[:k])
        arr_counts = 1 if ( float(k_running_sum)/k ) >= threshold else 0

        for up in range( k, len(arr)):
            dn = up - k
            k_running_sum -= arr[dn]
            k_running_sum += arr[up]
            arr_counts += 1 if ( float(k_running_sum) / k ) >= threshold else 0

        return arr_counts


if __name__ == "__main__":

    sol = Solution()
    print( sol.numOfSubarrays([2,2,2,2,5,5,5,8], 3, 4) )