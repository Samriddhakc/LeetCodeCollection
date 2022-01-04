"""
Q13.
Given an integer array nums and two integers firstLen and secondLen, return the maximum sum of elements in two non-overlapping subarrays with lengths firstLen and secondLen.
The array with length firstLen could occur before or after the array with length secondLen, but they have to be non-overlapping.
A subarray is a contiguous part of an array.
"""


class Solution(object):
    def maxSumTwoNoOverlap(self, nums, firstLen, secondLen):
        """
        :type nums: List[int]
        :type firstLen: int
        :type secondLen: int
        :rtype: int
        """
        def maxWindowSum( arr, length ):

            '''
            :param arr:
            :param len:
            :return: max_sum, lb, rb
            '''
            if len(arr) < length:
                return 0

            max_sum = sum(arr[:length])
            curr_sum = sum(arr[:length])
            lb = 0
            rb = length
            for r in range(length, len(arr)):
                curr_sum -= arr[r - length]
                curr_sum += arr[r]
                if (curr_sum > max_sum):
                    lb, rb = r - length, r

            return max_sum, lb, rb

        max_sum_1, lb_1, rb_1 = maxWindowSum( nums, max(firstLen, secondLen) )
        max_sum_2, lb_2, rb_2 = maxWindowSum( nums[:lb_1], min(firstLen, secondLen) )
        max_sum_3, lb_3, rb_3 = maxWindowSum( nums[rb_1 + 1:], min(firstLen, secondLen) )

        possible_1 = max( max_sum_2, max_sum_3 ) + max_sum_1

        max_sum_4, lb_4, rb_4 = maxWindowSum(nums, min(firstLen, secondLen))
        max_sum_5, lb_5, rb_5 = maxWindowSum(nums[:lb_4], max(firstLen, secondLen))
        max_sum_6, lb_6, rb_6 = maxWindowSum(nums[rb_4 + 1:], max(firstLen, secondLen))

        possible_2 = max(max_sum_5, max_sum_6) + max_sum_4

        return max(possible_2, possible_1)




        # [1, 2, 3, 4]
        # [100, 1, 7, 8] = max( 100 + 7 + 8, 100 + 1 + 8 )





if __name__ == "__main__":

    '''
    Call the solution method here. 
    '''

