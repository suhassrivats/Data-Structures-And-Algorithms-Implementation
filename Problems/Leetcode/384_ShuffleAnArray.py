import random


class Solution:

    def __init__(self, nums: List[int]):
        self.original = nums

    def reset(self) -> List[int]:
        """
        Resets the array to its original configuration and return it.
        """
        return self.original

    def shuffle(self) -> List[int]:
        """
        Returns a random shuffling of the array.
        """
        # It is important to copy the list in [:] format.
        # Read https://www.programiz.com/python-programming/methods/list/copy
        ans = self.original[:]  # copy list
        for i in range(len(ans)):
            j = random.randrange(0, len(ans))  # generate random index
            ans[i], ans[j] = ans[j], ans[i]  # swap
        return ans


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()
