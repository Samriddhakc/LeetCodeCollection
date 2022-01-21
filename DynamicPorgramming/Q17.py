class Solution:
    def numTeams(self, rating ) -> int:

        #         cache_increase = {}

        #         cache_decrease = {}

        #         def _numTeamsIncrease( count_pair, prev_idx ):

        #             if count_pair == 0:

        #                 return 1

        #             if (count_pair, prev_idx) in cache_increase:

        #                 return cache_increase[(count_pair, prev_idx)]

        #             total_count = 0

        #             for idx in range( prev_idx + 1 , len(rating) ):

        #                 if rating[idx] > rating[ prev_idx ] :

        #                     total_count += _numTeamsIncrease( count_pair - 1, idx )

        #             cache_increase[(count_pair, prev_idx)] = total_count

        #             return  cache_increase[(count_pair, prev_idx)]

        #         def _numTeamsDecrease( count_pair, prev_idx ):

        #             if count_pair == 0:

        #                 return 1

        #             if ( count_pair, prev_idx ) in cache_decrease:

        #                 return cache_decrease[( count_pair, prev_idx )]

        #             total_count = 0

        #             for idx in range( prev_idx + 1 , len(rating) ):

        #                 if rating[idx] < rating[ prev_idx ]:

        #                     total_count += _numTeamsDecrease( count_pair - 1, idx )

        #             cache_decrease[( count_pair, prev_idx )] = total_count

        #             return cache_decrease[( count_pair, prev_idx )]

        #         total = 0

        #         # Without cache, n * ( n + n - 1 + .....) = O ( n^3 ) time | O(1) space.
        #         # O(n^2) time | O(n^2) space.

        #         for start_idx in range( len(rating) ):

        #             total +=  _numTeamsIncrease( 2, start_idx ) + _numTeamsDecrease( 2, start_idx )

        #         return total

        # Best Approach not dp. O(N^2) time | O(1) space. 4

        total_count = 0

        for i in range(1, len(rating)):

            less_than = 0
            for j in range(0, i):
                if rating[j] < rating[i]:
                    less_than += 1

            greater_than = 0
            for k in range(i + 1, len(rating)):
                if rating[k] > rating[i]:
                    greater_than += 1

            total_count += (less_than * greater_than)

        for i in range(1, len(rating)):

            greater_than = 0
            for j in range(0, i):
                if rating[j] > rating[i]:
                    greater_than += 1

            less_than = 0
            for k in range(i + 1, len(rating)):
                if rating[k] < rating[i]:
                    less_than += 1

            total_count += ( less_than * greater_than )

        return total_count





