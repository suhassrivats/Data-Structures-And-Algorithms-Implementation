class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        """
        Time complexity:
            The time complexity of the above algorithm will be O(M+N) where ‘M’
        and ‘N’ are the lengths of the two input strings respectively.

        Space complexity:
            The algorithm runs in constant space O(1).
        """

        # use two-pointer approach to compare the strings
        index1 = len(S) - 1
        index2 = len(T) - 1

        while index1 >= 0 or index2 >= 0:
            i1 = self.get_next_valid_char_index(S, index1)
            i2 = self.get_next_valid_char_index(T, index2)
            if i1 < 0 and i2 < 0:  # reached end of both strings
                return True
            if i1 < 0 or i2 < 0:  # reached end of one of the strings
                return False
            if S[i1] != T[i2]:  # check if characters are equal
                return False

            index1 = i1 - 1
            index2 = i2 - 1

        return True

    def get_next_valid_char_index(self, string, index):
        backspace_count = 0
        while index >= 0:
            if string[index] == '#':  # found a backspace character
                backspace_count += 1
            elif backspace_count > 0:  # a non-backspace character
                backspace_count -= 1
            else:
                break
            index -= 1  # skip a backspace or a valid character
        return index
