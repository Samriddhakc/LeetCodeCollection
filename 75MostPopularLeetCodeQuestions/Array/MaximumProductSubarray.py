
class Solution:

    def maxProduct(self, nums):

        '''
        :param nums:
        :return:
        '''

        # Brute force solution. O(N) time | O(1) space
        # if not nums:
        #     return 0
        #
        # max_prod = -float('inf')
        # for s_idx in range(len(nums)):
        #     curr_prod = 1
        #     for e_idx in range(s_idx, len(nums)):
        #         curr_prod *= nums[e_idx]
        #         max_prod = max( max_prod, curr_prod )
        #
        # return max_prod

        # Keep two pointer, min_prod ( holds the minimum product), max_prod ( holds the maximum product ).
        # for any idx,
        # O(N) time | O(1) space.

        if not nums:
            return 0

        min_prod, max_prod, global_max = nums[0], nums[0], nums[0]

        for idx in range(1, len(nums)):
            prev_min = min_prod
            min_prod = min(min_prod * nums[idx], max_prod * nums[idx], nums[idx])
            max_prod = max(max_prod * nums[idx], prev_min * nums[idx], nums[idx])
            global_max = max(global_max, max_prod)

        return global_max


if __name__ == "__main__":

    sol = Solution()
    assert( sol.maxProduct([]) == 0 ) # empty list case
    assert( sol.maxProduct([1, 2, 3]) == 6 ) # all positive.
    print( sol.maxProduct([1, -2, 3]) )
    assert( sol.maxProduct([1, -2, 3]) == 3 ) # negative cases.
    assert( sol.maxProduct([-1, -2, -3]) == 6 ) #  all negative odd case.
    assert( sol.maxProduct([-1, -2, -3, -2]) == 12 ) #  all negative even case.
    assert( sol.maxProduct([-1, -2, -3, 2]) == 12 ) #  all negative even case.
    assert( sol.maxProduct([-1, -2]) == 2 ) #  single negative case.
    assert( sol.maxProduct([-1]) == -1 ) #  single negative case.








