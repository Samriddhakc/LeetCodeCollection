'''
You are given an array prices where prices[i] is the price of a given stock on the ith day.
You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.
Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0
'''

class Solution:
    def maxProfit(self, prices):

        # Big O. O(len(prices)) time | O(1) space
        '''
        :param prices:
        :return:
        '''

        max_profit = 0
        low_idx = 0
        for i in range(1, len(prices)):
            if (prices[i] < prices[low_idx]):
                low_idx = i
            else:
                max_profit = max(max_profit, prices[i] - prices[low_idx])

        return max_profit
    #         max_prof = 0
    #         for i in range(len(prices)):
    #             for j in range(i +1, len(prices)):
    #                 if prices[j] > prices[i]:
    #                     max_prof = max(max_prof, prices[j] - prices[i])
    #         return max_prof
