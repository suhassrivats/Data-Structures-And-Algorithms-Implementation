class Solution:
    def intervalIntersection(self, A: List[List[int]], B: List[List[int]]) -> List[List[int]]:
        """
        Time complexity:
            As we are iterating through both the lists once, the time complexity
        of the above algorithm is O(N + M), where ‘N’ and ‘M’ are the total
        number of intervals in the input arrays respectively.

        Space complexity:
            Ignoring the space needed for the result list, the algorithm runs
        in constant space O(1).
        """

        results = []
        i, j, start, end = 0, 0, 0, 1

        while i < len(A) and j < len(B):
            # check if the intervals overlap and if A[i]'s start time lies within the other intervals B[j]
            a_overlaps_b = A[i][start] >= B[j][start] and A[i][start] <= B[j][end]

            # check if the intervals overlap and if A[j]'s start time lies within the other intervals B[j]
            b_overlaps_a = B[j][start] >= A[i][start] and B[j][start] <= A[i][end]

            # store the intersection part
            if a_overlaps_b or b_overlaps_a:
                start_interval_intersection = max(A[i][start], B[j][start])
                end_interval_intersection = min(A[i][end], B[j][end])
                results.append([start_interval_intersection, end_interval_intersection])

            # move next from the interval which is finishing first
            if A[i][end] < B[j][end]:
                i += 1
            else:
                j += 1

        return results
