"""
Q12. Given a binary array nums, you should delete one element from it.
Return the size of the longest non-empty subarray containing only 1's in the resulting array. Return 0 if there is no such subarray.
"""

class Solution:

    def longestSubarray(self, nums):

        '''
        :param nums:
        :return:
        '''

        if 0 not in nums:
            return len(nums) - 1

        k = 1
        left, right = 0, 0
        max_len = 0
        curr_len = 0
        while (right < len(nums)):
            k -= (1 - nums[right])
            if (k == 0):
                curr_len = 0
                while (nums[left] > 0):
                    curr_len += 1
                    left += 1
                while ((right + 1) < len(nums) and nums[right + 1] > 0):
                    curr_len += 1
                    right += 1
                left += 1
                max_len = max(max_len, curr_len)
                k += 1
            right += 1

        return max_len






if __name__ == "__main__":
    sol = Solution()
    sol.longestSubarray()