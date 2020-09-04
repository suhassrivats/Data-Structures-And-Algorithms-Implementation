import heapq
"""
Definition of Interval.
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""


class Solution:
    """
    @param intervals: an array of meeting time intervals
    @return: the minimum number of conference rooms required

    Time complexity:
        The time complexity of the above algorithm is O(N*logN), where ‘N’ is
    the total number of meetings. This is due to the sorting that we did in the
    beginning. Also, while iterating the meetings we might need to poll/offer
    meeting to the priority queue. Each of these operations can take O(logN).
    Overall our algorithm will take O(NlogN).

    Space complexity:
        The space complexity of the above algorithm will be O(N) which is
    required for sorting. Also, in the worst case scenario, we’ll have to insert
    all the meetings into the Min Heap (when all meetings overlap) which will
    also take O(N) space. The overall space complexity of our algorithm is O(N).
    """

    def minMeetingRooms(self, intervals):
        if not intervals or len(intervals) == 0:
            return
        start, end = 0, 1
        # Sort intervals by start time
        intervals.sort(key=lambda x: x.start)
        min_heap = []  # store interval end times

        for interval in intervals:
            # If the start time of a new interval is greater than or equal to
            # the previous interval. In other words, if previous meeting has
            # ended, replace previous meeting end time with new meeting end time
            if min_heap and interval.start >= min_heap[0]:
                heapq.heapreplace(min_heap, interval.end)
            else:
                heapq.heappush(min_heap, interval.end)

        return len(min_heap)
