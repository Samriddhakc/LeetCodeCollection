"""
LongestConsecutiveSequence
"""

from collections import defaultdict

class Solution:

    def longestConsecutive(self, nums):

        '''
        :param nums:
        :return:
        '''

        #         if not nums:
        #             return 0

        #         max_len = 0
        #         curr_len = 1
        #         num_set = set(nums)

        #         for idx in range(len(nums)):

        #             if ( nums[idx] - 1 ) not in num_set:
        #                 curr_len = 1
        #                 current_num = nums[idx]

        #                 while  (current_num + 1) in num_set:
        #                     curr_len += 1
        #                     current_num += 1

        #             max_len = max( max_len, curr_len )

        #         return max_len

        graph = defaultdict(list)
        num_set = set(nums)

        for num in nums:
            if (num - 1) in num_set:
                graph[num - 1].append(num)
            else:
                graph["root"].append(num)

        max_len = 0
        dfs = [["root", 0]]

        visited = set()

        while dfs:
            curr_num, curr_len = dfs.pop()

            if not graph[curr_num]:
                max_len = max(max_len, curr_len)

            visited.add(curr_num)

            for nx_consecutive in graph[curr_num]:
                if nx_consecutive not in visited:
                    dfs.append([nx_consecutive, curr_len + 1])

        return max_len
        # nums.sort()
        #
        # if not nums:
        #     return 0
        #
        # max_len = 1
        # curr_len = 1
        #
        # for idx in range(len(nums) - 1):
        #
        #     if nums[idx + 1] == (nums[idx] + 1):
        #         curr_len += 1
        #
        #     elif nums[idx + 1] == nums[idx]: #edge case
        #         continue
        #
        #     else:
        #         max_len = max( max_len, curr_len )
        #         curr_len = 1
        #
        # return max( max_len, curr_len )


if __name__ == "__main__":
    sol = Solution()
