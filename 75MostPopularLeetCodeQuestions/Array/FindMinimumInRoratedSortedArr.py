
class  Solution:

    def findMin( self, nums ):

        '''
        :param nums:
        :return:
        '''

        # # Brute force sol.
        # return min(nums)

        # Big O. O(N) time | O(1) space.

        if not nums:
            raise ValueError("This case is not relevant for the question")

        if nums[0] <= nums[-1]:
            return nums[0]
        # log(n), binary search problem.
        l, r = 0, len(nums)
        while ( l <= r):

            mid = ( l + r )// 2
            print(mid)
            if ( nums[mid - 1] >= nums[mid] ):
                return nums[mid]

            if nums[0] <= nums[mid]:
                l = mid + 1 # go to the right.

            else:       # go to the left.
                r = mid

        # [5, 6, 1, 2, 3, 4]
        # [1, 1, 0]

if __name__ == "__main__":

    sol = Solution()
    # assert ( sol.findMin( [] ) === ? ) error handling in this case.
    # assert( sol.findMin([0]) == 0 )
    # assert( sol.findMin([0, 1, -1]) == -1 )
    assert( sol.findMin([-5, 0, 1]) == -5 )
    # assert( sol.findMin([0, 1, -5]) == -5 )
    # assert( sol.findMin([3, 1, 2]) == 1 )


