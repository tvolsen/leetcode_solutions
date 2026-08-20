# 1288. Remove Covered Intervals
class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        # sort by smallest starting value, and then largest ending value in ties
        intervals.sort(key=lambda x: (x[0], -x[1]))
        # we will lower this for each removable interval
        ans = len(intervals)
        # initial values
        prev_start, prev_end = intervals[0]
        # note the range starting at 1 because of initial values
        for i in range(1, len(intervals)):
            start, end = intervals[i]
            # if curr interval is subset, remove it
            if start >= prev_start and end <= prev_end:
                ans -= 1
            # update the new boundaries
            else:
                prev_start = start
                prev_end = end
        return ans
