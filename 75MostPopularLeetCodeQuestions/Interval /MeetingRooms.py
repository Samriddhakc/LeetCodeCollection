
class Room:

    def __init__(self, idx, start, end):
        self.idx = idx
        self.start = start
        self.end = end

class Solution:

    def canAttendMeetings( self, intervals ):

        '''
        :param intervals:
        :return:
        '''

        # Look for overlaps in intervlas.

        intervals.sort( key = lambda  x: x[0] ) # sort by start time

        for idx in range(len(intervals) - 1):
            c_interval =  intervals[idx]
            n_interval =  intervals[idx + 1]

            if c_interval[1] > n_interval[0]: # if the room is cleared before the next meeting
                return False

        return True



if __name__ == "__main__":
    sol = Solution()
    assert  ( sol.canAttendMeetings( [ [0, 10], [10, 20] ] ) == True )
    assert ( sol.canAttendMeetings(  [] ) == True )
    assert  ( sol.canAttendMeetings(  [ [ 0, 10 ] , [ 5, 20 ] ] ) == False )
    assert  ( sol.canAttendMeetings(  [ [ 0, 10 ] , [ 10, 20 ], [ 15, 30 ] ] ) == False )

