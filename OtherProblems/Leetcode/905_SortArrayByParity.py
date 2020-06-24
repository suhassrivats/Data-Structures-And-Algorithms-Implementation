class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        odd_index = 0
        index = 0

        while index < len(A) - 1:
            if A[index] % 2 != 0:
                if A[index+1] % 2 == 0:
                    A[odd_index], A[index+1] = A[index+1], A[odd_index]
                    odd_index += 1
                    index += 1
                else:
                    index += 1
            else:
                index += 1
                odd_index += 1

        return A
