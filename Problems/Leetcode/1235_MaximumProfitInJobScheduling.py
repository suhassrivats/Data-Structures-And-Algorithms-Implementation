from typing import List

class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        memo = {}  # Memoization dictionary to store computed results

        def get_next_index(jobs, l, cur_job_end):
            """Find the next job whose starting point >= currentJob's endpoint"""
            r = len(jobs) - 1
            result = len(jobs) + 1
            while (l <= r):
                mid = (l + r) // 2
                if jobs[mid][0] >= cur_job_end:
                    result = mid
                    r = mid - 1
                else:
                    l = mid + 1
            return result

        def solve(jobs, i):
            if i >= len(jobs):
                return 0

            if i in memo:  # Check if the result for the current index is already computed
                return memo[i]

            next_idx = get_next_index(jobs, i + 1, jobs[i][1])

            # Compute the profit for taking the current job or not taking it
            taken = jobs[i][2] + solve(jobs, next_idx)
            not_taken = solve(jobs, i + 1)

            # Store the maximum profit for the current index in the memoization dictionary
            memo[i] = max(taken, not_taken)

            return memo[i]

        # Start based on start time
        jobs = sorted(zip(startTime, endTime, profit), key=lambda x: x[0])

        return solve(jobs, 0)
