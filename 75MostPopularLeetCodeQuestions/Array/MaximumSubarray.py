class Solution:

    def maxSubArray(self, nums ):

        '''
        :param nums:
        :return:
        '''


        # Brute force method. O(N^2) time | O(1) space.
        # max_sum = -float('inf') # minimum among all the possible values
        # for s_idx in range(len(nums)):
        #     for e_idx in range( s_idx, len(nums)):
        #         max_sum = max( max_sum, sum(nums[s_idx: e_idx+1]) )
        #
        # return max_sum
        # O(N) time | O(1) space
        if not nums:
            return 0

        # Kandane's algorithm. # O(N) time | O(1) space
        max_sum = -float('inf')
        curr_sum = -float('inf')
        for idx in range(len(nums)):
            curr_sum = max( nums[idx], nums[idx] + curr_sum )
            max_sum = max(  max_sum, curr_sum )

        return max_sum



if __name__ == "__main__":

    sol = Solution()
    assert( sol.maxSubArray([]) == 0 )
    assert( sol.maxSubArray([1]) == 1 )
    assert( sol.maxSubArray([1, 2]) == 3 )
    assert( sol.maxSubArray([1, 2, -1, 13, 100]) == 115 )
    assert( sol.maxSubArray([1, 2, -100, 13, 100]) == 113 )
    assert (sol.maxSubArray([-1, -2, -3]) == -1)

