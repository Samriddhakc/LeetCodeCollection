"""
Q17. Grumpy Bookstore Owner
There is a bookstore owner that has a store open for n minutes. Every minute, some number of customers enter the store. You are given an integer array customers of length n where customers[i] is the number of the customer that enters the store at the start of the ith minute and all those customers leave after the end of that minute.
On some minutes, the bookstore owner is grumpy. You are given a binary array grumpy where grumpy[i] is 1 if the bookstore owner is grumpy during the ith minute, and is 0 otherwise.
When the bookstore owner is grumpy, the customers of that minute are not satisfied, otherwise, they are satisfied.
The bookstore owner knows a secret technique to keep themselves not grumpy for minutes consecutive minutes, but can only use it once.
Return the maximum number of customers that can be satisfied throughout the day.
"""

class Solution:
    def maxSatisfied(self, customers, grumpy, minutes ):

        # check the weight of Os in minutes window.
        # Maximize the weight of Os in that window period.
        # [1, 10, 1, 2, 3], [0, 1, 0, 1, 1], 2
        grumpy_wind = sum ( [ customers[i] for i,v in enumerate(grumpy[:minutes]) if grumpy[i] ] )
        max_wind = grumpy_wind
        for c_idx in range(minutes, len(customers)):
            grumpy_wind -= customers[c_idx-minutes] if grumpy[c_idx-minutes] else 0
            grumpy_wind += customers[c_idx] if grumpy[c_idx] else 0
            max_wind = max( max_wind, grumpy_wind )

        for idx, val in enumerate(grumpy):
            max_wind += customers[idx] if not val else 0

        return max_wind

if __name__ == "__main__":
    sol = Solution()
    print( sol.maxSatisfied( [1,0,1,2,1,1,7,5], [0,1,0,1,0,1,0,1], 3 ) )
