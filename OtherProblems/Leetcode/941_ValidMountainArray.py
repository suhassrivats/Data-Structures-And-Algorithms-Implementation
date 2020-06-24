class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        i = 0

        # Check for all increasing values
        while(i < len(A) and i+1 < len(A) and A[i] < A[i+1]):
            i += 1

        # If your pointer is still 0 (there is no increasing sequence) or if your pointer is at the end of the array (entire array is increasing) return false
        if (i == 0 or i+1 >= len(A)):
            return False

        # Otherwise, continue iterating through the remainder of the array ensuring it is strictly decreasing, if at any point it's not, return false.
        while(i < len(A) and i+1 < len(A)):
            if (A[i] <= A[i + 1]):
                return False
            i += 1

        return True
