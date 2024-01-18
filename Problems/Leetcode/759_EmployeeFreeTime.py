"""
# Definition for an Interval.
class Interval:
    def __init__(self, start: int = None, end: int = None):
        self.start = start
        self.end = end
"""

class Solution:
    # intervals = [[1,2],[1,3],[4,10],[5,6]]

    def employeeFreeTime(self, schedule: '[[Interval]]') -> '[Interval]':
        # Error checking
        if not schedule:
            return []

        # Store intervals in a single list
        intervals = []
        for employee in schedule:
            for interval in employee:
                intervals.append([interval.start, interval.end])

        # Sort intervals list by start time
        print(intervals)
        intervals.sort(key=lambda x: x[0])
        print(intervals)

        # Find free time
        result = []
        last_end = intervals[0][1]
        for i in range(1, len(intervals)):
            curr_start = intervals[i][0]
            curr_end = intervals[i][1]
            if curr_start > last_end:
                result.append(Interval(last_end, curr_start))
            last_end = max(last_end, curr_end)

        return result