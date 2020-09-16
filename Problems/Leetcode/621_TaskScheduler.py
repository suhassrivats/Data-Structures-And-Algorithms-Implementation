import heapq


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
        Time complexity:
            The time complexity of the above algorithm is O(N*logN) where ‘N’
        is the number of tasks. Our while loop will iterate once for each
        occurrence of the task in the input (i.e. ‘N’) and in each iteration we
        will remove a task from the heap which will take O(logN) time. Hence the
        overall time complexity of our algorithm is O(N*logN).

        Space complexity:
            The space complexity will be O(N), as in the worst case, we need to
        store all the ‘N’ tasks in the HashMap.
        """

        max_heap = []
        task_frequency_map = {}
        interval_count = 0

        for char in tasks:
            task_frequency_map[char] = task_frequency_map.get(char, 0) + 1

        # Add all tasks to the max heap
        for char, frequency in task_frequency_map.items():
            heapq.heappush(max_heap, (-frequency, char))

        while max_heap:
            # Try to execute as many as 'n+1' tasks from the max-heap. Because
            # 'n' denotes after doing a task X, wait for another n cycles before
            # you can schedule X. So, n+1 slots.
            k = n+1
            waitlist = []
            while k > 0 and max_heap:
                interval_count += 1
                frequency, char = heapq.heappop(max_heap)
                if -frequency > 1:
                    # decrement the frequency and add to the waitlist
                    waitlist.append((frequency+1, char))
                k -= 1

            # put all the waiting list back on the heap
            for frequency, char in waitlist:
                heappush(max_heap, (frequency, char))

            # why do you put an idle task? Why can't you schedule task A again?
            # Assume n = 2 (i.e., cool-down period is 2). So, once a task 'A'
            # is scheduled at time t, it can't be scheduled at t+1 and t+2. The
            # earliest it can be scheduled is t+3. We scheduled AB _ .
            # Here A can not be put at t+2.
            if max_heap:
                interval_count += k  # we'll be having 'k' idle intervals for the next iteration

        return interval_count
