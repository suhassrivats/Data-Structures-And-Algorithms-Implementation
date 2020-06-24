class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """

        i = 0
        while i < len(arr)-1:
            if arr[i] == 0:
                arr.insert(i+1, 0)
                del arr[len(arr)-1]
                i = i + 2
            else:
                i = i + 1
