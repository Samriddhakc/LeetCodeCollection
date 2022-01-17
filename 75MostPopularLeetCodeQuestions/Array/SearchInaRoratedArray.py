
class Solution:

    def search( self, nums, target ):

        '''
        :param nums:
        :param target:
        :return:
        '''

        # Brute force solution is just use linear search to find the target.
        # Cases based on pivot direction.
        # If pivot is in the right, and target < nums[mid], go to the left. else go to the right.
        # Reverse this step.
        if not nums:
            return -1

        l, r = 0, len(nums) - 1

        while ( l <= r ):

            mid = ( l + r)//2
            print( l , mid, r )
            if nums[mid] == target:
                return mid

            # pivot to the right, then [left.....mid] is sorted
            if nums[l] <= nums[mid]:

                # if target is < nums[mid], same as binary search intuition, you can go to the left to search
                if ( nums[l] <= target < nums[mid] ):
                    r = mid

                # else go to the right.
                else:
                    l = mid + 1

            # pivot is to the left, then [mid + 1,.... right is sorted]
            else:

                # if target is > nums[mid], same as binary search intuition, you can go to the right to search
                if (nums[r] >= target > nums[mid] ):

                    l = mid + 1

                else:

                    r = mid

        return -1


if __name__ == "__main__":

    sol = Solution()
    assert ( sol.search( [], 100 ) == -1 )
    assert ( sol.search( [1, 2], 1 )  == 0 )
    assert ( sol.search( [1, 2, 3], 3 )  == 2 )
    assert ( sol.search( [1, -2, 3], -2 )  == 1 )
    assert ( sol.search([4,5,6,7,0,1,2], 100) == -1 )
