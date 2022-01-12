"""
You are given an integer n. A 0-indexed integer array nums of length n + 1 is generated in the following way:
nums[0] = 0
nums[1] = 1
nums[2 * i] = nums[i] when 2 <= 2 * i <= n
nums[2 * i + 1] = nums[i] + nums[i + 1] when 2 <= 2 * i + 1 <= n
Return the maximum integer in the array nums​​​.


"""



class Solution:
    def getMaximumGenerated( self, n ):

        # '''
        # :param n:
        # :return:
        # '''
        # cache = {}
        # def getElement(n):
        #
        #     if n == 0:
        #         return 0
        #
        #     if n == 1:
        #         return 1
        #
        #     if n in cache:
        #
        #         return cache[n]
        #
        #     if n % 2 == 0:
        #         ans = getElement(n//2)
        #
        #     else:
        #         x = n//2
        #         ans = getElement(x) + getElement(x+1)
        #
        #     cache[n] = ans
        #     return cache[n]
        #
        # ans = [] # O( n ** 2 ^n ) => O(n + n) time | O(n) space.
        # for i in range(n+1):
        #     ans.append(getElement(i))
        #
        # return ans

        if n <= 1:
            return n
        ans = [0, 1]
        for i in range(2, n + 1):
            if i % 2 == 0:
                ans.append(ans[i // 2])
            else:
                x = i // 2
                ans.append(ans[x] + ans[x + 1])
        return max(ans)


if __name__ == "__main__":
    sol = Solution()



