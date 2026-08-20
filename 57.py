# 57. Insert Interval
class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals) == 0:
            return [newInterval]
        new_start = newInterval[0]
        idx = -1
        for i in range(len(intervals)):
            if new_start < intervals[i][0]:
                idx = i
                break
        if idx == -1:
            intervals.append(newInterval)
        else:
            intervals.insert(idx, newInterval)
        ans = []
        start, end = intervals[0]
        for i in range(1, len(intervals)):
            if intervals[i][0] <= end:
                end = max(end, intervals[i][1])
            else:
                ans.append([start, end])
                start, end = intervals[i]
        ans.append([start, end])
        return ans


        
