# Q3. Diet Plan Performance
# A dieter consumes calories[i] calories on the i-th day.
#
# Given an integer k, for every consecutive sequence of k days (calories[i], calories[i+1], ..., calories[i+k-1] for all 0 <= i <= n-k), they look at T, the total calories consumed during that sequence of k days (calories[i] + calories[i+1] + ... + calories[i+k-1]):
#
# If T < lower, they performed poorly on their diet and lose 1 point;
# If T > upper, they performed well on their diet and gain 1 point;
# Otherwise, they performed normally and there is no change in points.
# Initially, the dieter has zero points. Return the total number of points the dieter has after dieting for calories.length days.
#
# Note that the total points can be negative.
#

class Solution:


    #  Big O(len(calories)) time | O(1) space
    #
    #
    #

    def dietPlanPerformance(self, calories, k, lower, upper):

        initial_cals = sum(calories[:k])
        global  total_points
        total_points = 0

        def keepTrackOfPoints( cal_sum ):

            global total_points
            if cal_sum < lower:
                total_points -= 1

            if cal_sum > upper:
                total_points += 1

        keepTrackOfPoints(initial_cals)
        for up_idx in range( k, len(calories) ):
            lo_idx = up_idx - k
            initial_cals -= calories[lo_idx]
            initial_cals += calories[up_idx]
            keepTrackOfPoints( initial_cals )

        return total_points

if __name__ == "__main__":
    sol = Solution()
    print(  sol.dietPlanPerformance( [1,1,1], 2, 0, 1)  )
    assert( sol.dietPlanPerformance( [1,1,1], 2, 0, 1) == 2 )

