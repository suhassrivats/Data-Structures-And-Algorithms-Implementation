class Solution:
    def compress(self, chars: List[str]) -> int:
        """
        Complexity Analysis:
            Time Complexity: O(N), where N is the length of chars.
            Space Complexity: O(1), the space used by i, j, wptr.
        """

        i = 0
        wptr = 0
        while i < len(chars):
            j = i  # j will count the number of occurences of a character
            while j < len(chars) and chars[i] == chars[j]:
                j += 1
            freq = j - i

            # Write the character first and frequency next
            chars[wptr] = chars[i]
            wptr += 1

            # Write freq only if it is greater than 1
            if freq > 1:
                for digit in str(freq):
                    chars[wptr] = digit
                    wptr += 1

            # Once char and its freq is printed, move to next unique char
            i = j
        return wptr
