class Solution:

    def containsDuplicate( self, nums ):

        '''
        :param nums:
        :return:
        '''

        # # Brute force. O(N^2) time | O(1) space
        # for idx, num in enumerate(nums):
        #     if num in nums[idx+1:]:
        #         return True
        #
        # return False
        # O(N) time | O(n) space
        seen_el = set()
        for num in nums:
            if num in seen_el:
                return True
            seen_el.add(num)
        return False


if __name__ == "__main__":

    sol = Solution()
    assert( sol.containsDuplicate( [] ) == False )
    assert ( sol.containsDuplicate( [1] ) == False )
    assert ( sol.containsDuplicate( [1, 1] ) == True )
    assert ( sol.containsDuplicate( [1, 1, 2, 2] ) == True )
    assert ( sol.containsDuplicate( [1, 1, 2, 3] ) == True )


