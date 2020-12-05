class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        results = [None] * len(A)
        left, right = 0, len(A)-1

        for i in range(len(A)-1, -1, -1):  # Iterate from the end
            if abs(A[left]) < abs(A[right]):
                results[i] = A[right] ** 2
                right -= 1
            else:
                results[i] = A[left] ** 2
                left += 1

        return results
