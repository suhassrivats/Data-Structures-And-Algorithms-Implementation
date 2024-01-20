class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        visited = [False] * len(arr)

        def helper(arr, i):
            if i<0 or i>=len(arr):
                return False

            if arr[i] == 0:
                return True

            if visited[i]:
                return False

            visited[i] = True

            r = helper(arr, i+arr[i])
            l = helper(arr, i-arr[i])

            return r or l

        return helper(arr, start)