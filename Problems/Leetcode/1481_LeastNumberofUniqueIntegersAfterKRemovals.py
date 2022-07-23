import collections


class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        counter = collections.Counter(arr).items()
        num_freq_map = sorted(counter, key=lambda x: x[1])  # sort by value (frequency) - O(NlogN)
        print(num_freq_map)
        removed = 0  # number of removed items
        for num, freq in num_freq_map:
            if k >= freq:
                k -= freq
                removed += 1
            else:
                break
        return len(num_freq_map) - removed
