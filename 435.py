# 435. Non-overlapping Intervals
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        counter = 0
        intervals.sort(key=lambda x: x[1])
        prev_end = intervals[0][1]
        for i,interval in enumerate(intervals):
            if i == 0:
                continue
            else:
                start = interval[0]
                if start < prev_end:
                    counter += 1
                else:
                    prev_end = interval[1]
        return counter
