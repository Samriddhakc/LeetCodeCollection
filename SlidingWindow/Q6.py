"""
Q6.Given an integer array nums and an integer k, you are asked to construct the array ans of size n-k+1
 where ans[i] is the number of distinct numbers in the subarray nums[i:i+k-1] = [nums[i], nums[i+1], ..., nums[i+k-1]].
Return the array ans.
"""

from collections import Counter

class Solution:


    def distinctNumbers(self, nums, k):

        '''
        :param nums:
        :param k:
        :return:
        '''
        # nums = [1, 2, 3, 2, 2, 1, 3], k = 3
        num_hash = Counter(nums[:k])
        ans = [ len(num_hash) ]
        for up_idx in range(k, len(nums)):
            left_str = nums[up_idx - k]
            num_hash[left_str] -= 1
            if ( num_hash[left_str] == 0 ):
                num_hash.pop( left_str )
            num_hash[nums[up_idx]] += 1
            ans.append( len(num_hash)  )

        return ans

if __name__ == "__main__":
    sol = Solution()
    print( sol.distinctNumbers(  [1, 2, 3, 2, 2, 1, 3], 3) )

