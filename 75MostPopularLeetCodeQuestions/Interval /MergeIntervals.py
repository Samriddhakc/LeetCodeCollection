class Solution:
    def merge(self, intervals):

        def isOverLap(interval_1, interval_2):

            return (max(interval_1[0], interval_2[0]) <= min(interval_1[1], interval_2[1]))

        intervals.sort(key=lambda x: x[0])
        idx = 0
        res = []
        while idx < len(intervals):
            nx_idx = idx + 1
            lb, ub = intervals[idx][0], intervals[idx][1]
            while (nx_idx < len(intervals) and isOverLap([lb, ub], intervals[nx_idx])):
                lb, ub = min(lb, intervals[nx_idx][0]), max(ub, intervals[nx_idx][1])
                nx_idx += 1
            res.append([lb, ub])
            idx = nx_idx

        return res

