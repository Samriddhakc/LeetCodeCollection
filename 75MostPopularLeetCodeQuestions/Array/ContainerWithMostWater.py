
class Solution:

    def maxArea( self, height ):

        '''
        :param height:
        :return:
        '''
        # Brute force

        if not height:
            return 0

        l, r = 0, len(height) - 1
        max_area = 0
        while ( l <= r ):
            max_area = max( max_area, ( r - l ) * min( height[r], height[l] ) )
            if height[r] > height[l]:
                l += 1
            else:
                r -= 1

        return max_area
        #
        # max_area = -float('inf')
        # for start in range( len(height) ):
        #     for end in range ( start + 1, len(height) ):
        #         max_area = max( max_area, min(height[start], height[end]) * ( end - start ) )
        #
        # return max_area


if __name__ == "__main__":
    sol = Solution()
    assert ( sol.maxArea([]) == 0 )
    assert ( sol.maxArea([1, 2, 3]) == 2 )
    assert ( sol.maxArea([1, 50, 100]) == 50 )
