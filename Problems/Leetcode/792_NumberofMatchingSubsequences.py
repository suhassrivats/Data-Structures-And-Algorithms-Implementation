from collections import defaultdict
from bisect import bisect


class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        """
        T: O(N * Mlog(M))
        S: O(N)
        """
        lookup = defaultdict(list)
        result = 0

        # Store positions of a char
        for i, c in enumerate(s):
            lookup[c].append(i)

        def bs(lst, n):
            l, r = 0, len(lst)
            while l < r:
                mid = (l+r)//2
                if n < lst[mid]:
                    r = mid
                else:
                    l = mid+1
            return l

        for word in words:
            prev = -1
            found = True
            for c in word:
                # tmp = bisect(lookup[c], prev)
                tmp = bs(lookup[c], prev)
                if tmp == len(lookup[c]):
                    found = False
                    break
                else:
                    prev = lookup[c][tmp]
            if found:
                result += 1

        return result
