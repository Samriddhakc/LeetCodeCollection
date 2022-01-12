"""
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
A subarray is a contiguous part of an arra
"""

class Solution:

    def maxSubArray(self, nums):

        '''
        :param nums:
        :re
        turn:
        '''

        max_sum = -float('inf')
        local_sum = -float('inf')
        for i in range(len(nums)):
            local_sum += nums[i]
            local_sum = max(local_sum, nums[i])
            max_sum = max(max_sum, local_sum)

        return max_sum