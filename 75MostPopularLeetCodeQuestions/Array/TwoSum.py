
class Solution:

    def twoSum(self, nums, target):

        '''
        :param nums:
        :param target:
        :return:
        '''

        # Can it be same indices?
        # Can there be more than one pair of solution?
        # Can the input be empty?
        # Can there be no input with the answer?
        # * can be empty.
        # * return the first pair.
        # * yes.
        # * yes.

        # Brute force sol.
        # O(N^2) time | O(1) space.
        # for i in range(len(nums)):
        #     for j in range( i + 1, len(nums)):
        #         if ( ( nums[i] + nums[j] ) == target ):
        #             return [ i, j ]
        #
        # return []

        # O(N) time | O(N) space.
        hash_sum = {}
        for idx, num in enumerate(nums):
            if nums[idx] in hash_sum:
                return [ hash_sum[nums[idx]], idx ]
            hash_sum[target - nums[idx]] = idx

        return []





if __name__ == "__main__":

    sol = Solution()
    assert ( sol.twoSum( [1, 2], 3 ) == [0, 1] )
    assert ( sol.twoSum( [], 100) == [] )
    assert ( sol.twoSum([1], 100 )  == [] )
    assert ( sol.twoSum( [1, 2], 5 ) == [] )



