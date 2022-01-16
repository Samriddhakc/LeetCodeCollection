
class Solution:

    def productExceptSelf(self, nums):


        # Brute force ( O(N^2) time | O(1) extra space.
        # if num is empty.
        # if not nums:
        #     return []
        #
        # # if len is exactly 1, no product after self.
        # if len(nums) == 1:
        #     return [ 0 ]
        #
        # product_arr = []
        # for s_idx in range( len(nums)  ):
        #     curr_product = 1
        #     for e_idx in range( len(nums) ):
        #         if s_idx != e_idx:
        #             curr_product *= nums[e_idx]
        #     product_arr.append( curr_product )
        #
        # return product_arr

        if not nums:
            return []

        # if len is exactly 1, no product after self.
        if len(nums) == 1:
            return [ 0 ]

        left_prod =  [ 0 ] * ( len(nums) + 1 ) # idx, contains product until(increasing)/not including idx i.
        right_prod = [ 0 ] * ( len(nums) + 1 ) # idx, contains product until(decreasing)/ including idx i.

        # left_prod = [1, 1, 2]
        # right_prod = [2, 2,1]
        left_prod[0] = 1
        right_prod[-1] = 1

        prod_arr = []

        for idx in range( len(nums) ):
            left_prod[idx + 1] = left_prod[idx] * nums[idx]
            right_prod[ len(nums) - idx - 1 ] = right_prod[ len(nums) - idx ] * nums[  len(nums) - idx - 1  ]

        for idx in range(len(nums)):
            prod_arr.append( left_prod[idx] *  right_prod[idx + 1] ) # idx not included.

        return prod_arr
        # Optimization of space.
        # if not nums:
        #     return []
        #
        # # if len is exactly 1, no product after self.
        # if len(nums) == 1:
        #     return [0]
        #
        # prod_arr = [0] * len(nums)
        # prod_arr[0] = 1
        #
        # for idx in range(1, len(prod_arr)):
        #     prod_arr[idx] = nums[idx - 1] * prod_arr[idx - 1]
        #
        # R = 1
        # for idx in reversed(range(len(prod_arr))):
        #     prod_arr[idx] = prod_arr[idx] * R
        #     R *= nums[idx]
        #
        # return prod_arr


if __name__ == "__main__":

    sol = Solution()
    assert ( sol.productExceptSelf([]) == [] )
    assert ( sol.productExceptSelf([1]) == [0]  )
    assert ( sol.productExceptSelf([1, 2]) == [2, 1]  )
    assert ( sol.productExceptSelf([1, 2, 3]) == [6, 3, 2]  )


