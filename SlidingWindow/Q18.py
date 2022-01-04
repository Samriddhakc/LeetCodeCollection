"""
Q18. Kth Smallest Subarray Sum
Given an integer array nums of length n and an integer k, return the kth smallest subarray sum.
A subarray is defined as a non-empty contiguous sequence of elements in an array. A subarray sum is the sum of all elements in the subarray.
"""


class Solution:

    def numSubArraysLessThanEqualsVal(self, arr, val):
        # [1, 2, 3]
        #  |  |
        num_arr = 0
        l, r = 0, 0
        curr_sum = 0
        while ( l < len(arr) ):
            idx = 0
            while ( r < len(arr) and curr_sum <= val ):
                curr_sum += arr[r]
                r += 1
                idx += 1
            if ( idx > 0):
                num_arr += ( idx - 1 )
            curr_sum -= arr[l]
            l += 1

        return num_arr


    # [1, 2, 3] = 1, 2, 3, 3, 5, 6
    def kthSmallestSubarraySum(self, nums, k):

        """
        :param nums:
        :param k:
        :return:
        """

        l, r = 0, sum(nums)
        while ( l <= r ):
            mid = (l + r)//2
            if ( self.numSubArraysLessThanEqualsVal(nums, k) == k ):
                return mid
            if ( self.numSubArraysLessThanEqualsVal(nums, k) < k ):
                l = mid + 1
            else:
                r = mid - 1
        return mid


        # Observation 1: [1, 2, 3]
        # 1, 2, 3, 3, 5, 6. How many contingious sub arrays are there with sum <= k?
        #print( numSubArraysLessThanEqualsVal( nums, k) )

if __name__ == "__main__":
    sol = Solution()
    print(sol.numSubArraysLessThanEqualsVal([3, 3, 5, 5], 10))
    #print( sol.kthSmallestSubarraySum ( [3, 3, 5, 5],  7) )
    #print(sol.kthSmallestSubarraySum([1,2,3], 1))
    # [1], [2], [3], [1,2].
    # 3, 3, 6, 5, 5, 8, 8, 10.