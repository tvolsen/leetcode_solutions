# 56. Merge Intervals
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # sort by starting value
        intervals.sort(key=lambda x: x[0])
        ans = []
        # store first seen start and end
        curr_start, curr_end = intervals[0]
        # loop over all other intervals
        for i in range(1, len(intervals)):
            start, end = intervals[i]
            # if new start <= curr_start, ie they overlap, union them
            if start <= curr_end:
                curr_end = max(curr_end, end)
            # if they do not overlap, add union to ans
            else:
                ans.append([curr_start, curr_end])
                # start new union of intervals
                curr_start = start
                curr_end = end
        # add the final union to ans
        ans.append([curr_start, curr_end])
        return ans
