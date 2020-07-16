"""
We just keep track of the index of the added elements, so when we remove them,
we copy the last one into it.

From Python docs (https://wiki.python.org/moin/TimeComplexity) we know that
list.append() takes O(1), both average and amortized. Dictionary get and set
functions take O(1) average, so we are OK.
"""
import random


class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums = []
        self.pos = {}

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already
        contain the specified element.
        """
        if val not in self.nums:
            self.nums.append(val)
            self.pos[val] = len(self.nums) - 1
            return True
        return False

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the
        specified element.
        """
        if val in self.pos:
            index = self.pos[val]  # get the val index
            last = self.nums[-1]  # get the last addition
            self.nums[index] = last
            self.pos[last] = index
            self.nums.pop()
            del self.pos[val]
            return True
        return False

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return self.nums[random.randint(0, len(self.nums) - 1)]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
