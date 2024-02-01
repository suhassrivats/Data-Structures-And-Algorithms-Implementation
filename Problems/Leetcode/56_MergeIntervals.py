class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        Time complexity:
            The time complexity of the above algorithm is O(N * logN), where ‘N’
        is the total number of intervals. We are iterating the intervals only
        once which will take O(N), in the beginning though, since we need to
        sort the intervals, our algorithm will take O(N * logN).

        Space complexity:
            The space complexity of the above algorithm will be O(N) as we need
        to return a list containing all the merged intervals. We will also need
        O(N) space for sorting. Python uses Timsort and it needs O(N) space.
        Overall, our algorithm has a space complexity of O(N).
        """

        if len(intervals) < 2:
            return intervals

        # sort intervals based on start time
        intervals = sorted(intervals, key=lambda x: x[0])

        merged_intervals = []
        start = intervals[0][0]
        end = intervals[0][1]

        for i in range(1, len(intervals)):
            interval = intervals[i]
            if interval[0] <= end:  # overlapping intervals, adjust the end
                end = max(interval[1], end)
            else:  # non-overlapping interval, add the previous interval and reset
                merged_intervals.append([start, end])
                start = interval[0]
                end = interval[1]

        # add the last interval
        merged_intervals.append([start, end])

        return merged_intervals
