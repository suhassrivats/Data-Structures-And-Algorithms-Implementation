# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7

class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        index = 41  # We are ignoring all indexes after 41
        while index > 40:
            index = (rand7()-1) * 7 + rand7()
        return ((index-1) % 10) + 1
