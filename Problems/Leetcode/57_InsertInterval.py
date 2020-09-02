class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        """
        Time complexity:
            As we are iterating through all the intervals only once, the time
        complexity of the above algorithm is O(N), where ‘N’ is the total
        number of intervals.

        Space complexity:
            The space complexity of the above algorithm will be O(N) as we need
        to return a list containing all the merged intervals.
        """

        merged = []
        i, start, end = 0, 0, 1

        # skip (and add to output) all intervals that come before the 'newInterval'
        # [[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]
        while i < len(intervals) and intervals[i][end] < newInterval[start]:
            merged.append(intervals[i])
            i += 1

        # merge all intervals that overlap with newInterval
        while i < len(intervals) and intervals[i][start] <= newInterval[end]:
            newInterval[start] = min(intervals[i][start], newInterval[start])
            newInterval[end] = min(intervals[i][end], newInterval[end])
            i += 1

        # insert the new interval
        merged.append(newInterval)

        # add all the remaining intervals to the output
        while i < len(intervals):
            merged.append(intervals[i])
            i += 1

        return merged
