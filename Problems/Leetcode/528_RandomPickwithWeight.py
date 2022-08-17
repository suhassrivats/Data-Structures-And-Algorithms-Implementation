import random


class Solution:
    """
    w = [1,3,4,5,2]

    0 1   4    8     13 15     
    |=|===|====|=====|==|

    Range  Numbers in that range
    0-1:   1
    1-4:   2,3,4
    4,8:   5,6,7,8
    8-13:  9,10,11,12,13
    13-15: 14,15

    Idea:
        - Store cumulative weight in an array. In this example, it will store [1,4,8,13,15]
        - Use random function to pick an integer from (1,total-sum)
        - For each integer, return the index of the range that it will fit in. If the randint=2, then return index=2
            as 2 will fall in the range 1-4. 4 is the second element.
        - Since the range is in increasing order, we can use binary search to find it.
    """

    def __init__(self, w: List[int]):
        self.w_cum = []
        self.sum = 0
        # Store cumulative weight in an array
        for i in w:
            self.sum += i
            self.w_cum.append(self.sum)

    def pickIndex(self) -> int:
        val = random.randint(1, self.sum)
        return self.binarySearch(val)

    def binarySearch(self, val):
        l, r = 0, len(self.w_cum)-1
        while l < r:
            mid = (l+r)//2
            if self.w_cum[mid] < val:
                l = mid+1
            else:
                r = mid
        return l
