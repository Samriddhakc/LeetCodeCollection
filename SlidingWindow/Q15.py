"""
Q15.Count Number of Nice Subarrays.
Given an array of integers nums and an integer k. A continuous subarray is called nice if there are k odd numbers on it.
Return the number of nice sub-arrays.
"""

class Solution:

    def numberOfSubArrays(self, nums, k):

        '''
        :param nums:
        :param k:
        :return:
        '''

        left, right = 0, 0
        num_nice = 0
        while ( right < len(nums) ):

            k -= nums[right] % 2

            if k == 0:

                left_offset, right_offset  = 1, 1

                while (nums[left] % 2 == 0):
                    left_offset += 1
                    left += 1

                k += nums[left] % 2
                left += 1

                while ( (right + 1) < len(nums) and nums[right+1] % 2 == 0):
                    right_offset += 1
                    right += 1
                num_nice += ( left_offset * right_offset )
                left_offset, right_offset = 1, 1

            right += 1

        return num_nice


if __name__ == "__main__":
    '''
    call the solution method for solutions 
    '''
    sol = Solution()
    #print( sol.numberOfSubArrays([1,1,2,1,1], 3) )
    print( sol.numberOfSubArrays([2,2,1,2,2], 1) )
    print ( sol.numberOfSubArrays( [2,2,2,1,2,2,1,2,2,2], 2) )

    # [2,2,1,2,2]
    # [1], [2,1], [2,2,1], [1,2], [2,1,2], [1,2,2], [2,1,2,2], [2,2,1,2],[2,2,1,2,2]
