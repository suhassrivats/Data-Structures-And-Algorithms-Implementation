import collections
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
        Idea:
            To allocate high freq tasks at the earliest. Put high freq tasks in a max-heap. Pop one by one and popped
            item to queue by decrementing its frequency by 1. To the queue add another param with the timeslot. Timeslot
            will be time at which it was popped+n.
            Ex: q = [[-2,A,2]] where -2 is freq after dec by 1. 2 is the timeslot at which this item needs to be added.
        """

        # Put freq,task in max_heap
        char_freq_map = collections.Counter(tasks)
        max_heap = [(-f,c) for c,f in char_freq_map.items()]
        heapq.heapify(max_heap)

        # units of times counter
        time_counter = 0
        q = collections.deque()

        # Pop elements from heap and increment the counter
        while max_heap or q:
            time_counter += 1

            if max_heap:
                f,c = heapq.heappop(max_heap)
                f = 1 + f
                if f != 0:
                    q.append([f, c, time_counter+n])

            # The item in the q is ready to be added back to the heap when its timeslot is same as max_heap time_counter
            if q and q[0][2] == time_counter:
                f, c, t = q.popleft()
                heapq.heappush(max_heap, (f,c))

        return time_counter