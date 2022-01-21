class Solution:

    def isOverlap(self, interval_1, interval_2):

        return (max(interval_1[0], interval_2[0]) <= min(interval_1[1], interval_2[1]))

    def insert(self, intervals, newInterval ):

        if not intervals or not newInterval:
            if not intervals:
                return [newInterval]
            if not newInterval:
                return intervals

        idx = 0
        res = []
        isInsert = False

        while (idx < len(intervals)):

            if self.isOverlap(intervals[idx], newInterval): # mix all overlapping intervals in a greedy manner.

                lb, ub = newInterval[0], newInterval[1]

                while idx < len(intervals) and self.isOverlap(intervals[idx], newInterval):
                    lb = min(lb, intervals[idx][0])
                    ub = max(ub, intervals[idx][1])
                    idx += 1

                res.append([lb, ub])
                isInsert = True
                break

            else:

                if (not isInsert and intervals[idx][0] > newInterval[0]): # If interval start is less than curr_idx insert.

                    res.append(newInterval)
                    res.append(intervals[idx])
                    isInsert = True


                else: # just copy as is.

                    res.append(intervals[idx])

            idx += 1

        for i in range(idx, len(intervals)):
            res.append(intervals[i])

        if not isInsert:
            res.append(newInterval)

        return res


if __name__ == "__main__":

    sol = Solution()

    assert  ( sol.insert( [ [] ], [] ) == [ [] ] )
    assert  ( sol.insert( [ [1, 3] ], [] ) == [ [1, 3] ] )
    assert ( sol.insert( [ [1, 3] ], [2, 5] ) == [ [1, 5] ] )
    assert  ( sol.insert( [ [1, 3], [6, 9] ], [2, 5] ) == [ [1, 5], [6, 9] ] )
    assert  ( sol.insert( [ [1, 3], [6, 9] ], [2, 7] ) == [ [1, 9 ] ] )


