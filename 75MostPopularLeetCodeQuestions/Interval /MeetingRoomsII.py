import heapq

class Solution:

    def minMeetingRooms( self, intervals ):

        '''
        :param intervals:
        :return:
        '''
        #
        # def isOverLap( interval1, interval2 ):
        #
        #     return ( ( interval1[0] <= interval2[0] and interval2[1] < interval1[1] )
        #                 or ( interval2[0] <= interval1[0] and interval1[1] < interval2[1] )  )
        #
        #
        # # O(N^2) time | O(1) space
        #
        # if not intervals:
        #     return 0
        #
        # max_overlap  = 0
        #
        # for idx_1 in range(len(intervals)):
        #     curr_overlap = 0
        #     for idx_2 in range(len(intervals)):
        #         if idx_1 != idx_2:
        #             if isOverLap( intervals[idx_1], intervals[idx_2] ):
        #                 curr_overlap += 1
        #
        #     max_overlap = max( max_overlap, curr_overlap )
        #
        # return max_overlap + 1

        # Solution 2. Sort by start time and be greedy.
        # intervals.sort( key = lambda  x: x[0] )
        #
        # for idx in range( len(intervals) )

        # Solution 3: Use min heap to keep track of meeting that ends next.
        intervals.sort( key = lambda x: x[0] )
        hp = []
        for inter in intervals:
            if hp and hp[0] <= inter[0]: # end time < start_time for next.
                heapq.heappop( hp )
                heapq.heappush( hp, inter[1]  )
            else:
                heapq.heappush( hp, inter[1] )



        return len(hp)


if __name__ == "__main__":

    sol = Solution()
    sol.minMeetingRooms( [ [1, 2], [1, 3], [3, 4] ] )
    assert ( sol.minMeetingRooms( [] ) == 0 )
    assert ( sol.minMeetingRooms( [ [1, 2], [3, 4] ] ) == 1 )
    assert  ( sol.minMeetingRooms( [ [1, 2], [1, 3], [3, 4] ] ) == 2 )
    assert  ( sol.minMeetingRooms( [ [1, 2], [1, 3], [2, 4] ]) == 2 )
    assert ( sol.minMeetingRooms( [ [1, 2], [1, 3], [1, 4] ] ) == 3 )

