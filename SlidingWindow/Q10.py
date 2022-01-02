"""
Q10.Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the
 array if you can flip at most k 0's.
"""

class Solution:
    def longestOnes(self, nums, k):

        '''
        :param nums:
        :param k:
        :return:
        '''
        # Find the max num of consecutive ones if you can flip at most k 0s.
        # Keep track of window size by counting number of Os.
        # [0, 0, 1, 0, 1] l = 1.
        #  |
        left = 0
        max_size = 0
        for right in range(len(nums)):
            k -= ( 1 - nums[right] )

            if ( k < 0 ):
                max_size = max(max_size, right - left )
                while ( left < len(nums) and nums[left] > 0 ):
                    left += 1
                k += 1
                left += 1


        return max_size


if __name__ == "__main__":
    sol = Solution()
    print( sol.longestOnes([1,1,1,0,0,0,1,1,1,1,0], 2) )
    print( sol.longestOnes(  [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1],  3 ) )
