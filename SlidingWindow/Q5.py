"""
Q5.
You are given an integer array nums consisting of n elements, and an integer k.
Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.
"""

class Solution:

    def findMaxAverage(self, nums, k):

        """
        :param nums:
        :param k:
        :return:
        """

        curr_sum = sum(nums[:k])
        max_avg = curr_sum/k

        for up_ptr in range( k, len(nums) ):
            lp_ptr = up_ptr - k
            curr_sum -= nums[lp_ptr]
            curr_sum += nums[up_ptr]
            max_avg = max( max_avg, curr_sum/k )

        return max_avg


if __name__ == "__main__":
    sol = Solution()
    print ( sol.findMaxAverage( [1,12,-5,-6,50,3], 4) )
