import heapq


class Solution:

    def eraseOverlapIntervals( self, intervals ):

        '''
        :param intervals:
        :return:
        '''
        def hasOverlap( inter ):

            for idx in range( len(inter) - 1 ):
                curr_inter, next_inter = inter[idx], inter[idx + 1]
                if max( curr_inter[0],next_inter[0] ) < min( curr_inter[1], next_inter[1] ):
                    return True
            return False

        def numOverLap( intervals, i_idx ):
            count = 0
            for idx in range(len(intervals)):
                if i_idx != idx:
                    if max(intervals[idx][0], intervals[i_idx][0]) >= min(intervals[idx][1], intervals[i_idx][1]):
                        break
                    count += 1
            return count

        if not intervals:
            return  0

        intervals.sort()
        hp = [ ( -numOverLap( intervals, idx ), idx ) for idx  in range(len(intervals))  ]
        heapq.heapify( hp )
        min_removals = 0
        while len(hp) > 1:
            overlap, i_idx = heapq.heappop(hp)
            if overlap == 0:
                break
            min_removals += 1
            if not hasOverlap(intervals[:i_idx] + intervals[i_idx + 1:]):
                break
        return min_removals





if __name__ == "__main__":

    sol = Solution()
    assert( sol.eraseOverlapIntervals( [ [] ]) == 0 )
    assert( sol.eraseOverlapIntervals( [ [1, 2], [3, 4] ] )  == 0 )
    assert( sol.eraseOverlapIntervals( [ [1, 2], [1, 4] ] )  == 1 )
    assert( sol.eraseOverlapIntervals( [ [1, 2], [1, 4], [3, 4] ] )  == 1 )
    assert( sol.eraseOverlapIntervals( [ [1, 2], [1, 4], [1, 5] ] )  == 2 )
    assert( sol.eraseOverlapIntervals( [ [1, 2], [1, 4], [1, 5], [ 8, 9], [ 8, 10] ] )  == 3 )







