from collections import defaultdict
from bisect import bisect


class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        """
        Idea:
            - Store chars in s and its occurences in a map. This way we don't have to iterate
            through entire "s" to find the indices of a particular char.
            a: [0]
            b: [1]...
            - For each char in word, check if the char exists. 
            - Also, note that we need to keep track of prev index so that next occurence of the same char should be greater than prev-index.

            Example:
            s = "aabc", w=aba
            a: [0,1]
            b: [2]
            c: [3]

            Here, we can't consider "a" at position 1 as it appears before b.

        T: O(N * Mlog(M))
        S: O(N)
        """

        lookup = defaultdict(list)
        count = 0

        # char: [list, of, its, locations]
        for i, s in enumerate(s):
            lookup[s].append(i)

        for word in words:
            prev = -1
            found = True
            for c in word:
                # Since we need to find the index greater than our prev, it is best that we use Binary Search
                # only check in particular char indices, starting from prev index
                tmp = bisect(lookup[c], prev)
                # If we have traversed the entire list, then we don't have a subsequence
                if tmp == len(lookup[c]):
                    found = False
                    break
                else:
                    prev = lookup[c][tmp]  # update prev index position
            if found:
                count += 1

        return count
