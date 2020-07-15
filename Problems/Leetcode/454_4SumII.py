class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        dict = {}
        count = 0

        for a in A:
            for b in B:
                sum = c + d
                dict[sum] = dict.get(sum, 0) + 1

        for c in C:
            for d in D:
                sum = -(c + d)
                if sum in dict:
                    count += dict[sum]

        return count
