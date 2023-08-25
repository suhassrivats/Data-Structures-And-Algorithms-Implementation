class Solution:
    def maxProduct(self, s: str) -> int:
        N, pali = len(s), {}  # bitmask: length

        for mask in range(0, 1<<N):  # Generate masks for all subsets
            subseq = ""
            for i in range(N):  # For all bits in bitmask of N-bits, check if bit is set
                if mask & (1<<i):
                    subseq += s[N - i - 1]
            if subseq == subseq[::-1]:
                pali[mask] = len(subseq)

        res = 0
        for m1 in pali:
            for m2 in pali:
                if m1 & m2 == 0:
                    res = max(res, pali[m1]* pali[m2])
        return res