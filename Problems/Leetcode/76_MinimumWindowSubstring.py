"""
Solution:
This problem follows the Sliding Window pattern and has a lot of similarities
with Permutation in a String with one difference. In this problem, we need to
find a substring having all characters of the pattern which means that the
required substring can have some additional characters and doesn’t need to be
a permutation of the pattern. Here is how we will manage these differences:

1) We will keep a running count of every matching instance of a character.
2) Whenever we have matched all the characters, we will try to shrink the
window from the beginning, keeping track of the smallest substring that has
all the matching characters.
3) We will stop the shrinking process as soon as we remove a matched character
from the sliding window. One thing to note here is that we could have redundant
matching characters, e.g., we might have two ‘a’ in the sliding window when we
only need one ‘a’. In that case, when we encounter the first ‘a’, we will
simply shrink the window without decrementing the matched count. We will
decrement the matched count when the second ‘a’ goes out of the window.

Time Complexity:
The time complexity of the above algorithm will be O(N+M) where ‘N’ and ‘M’
are the number of characters in the input string and the pattern respectively.

Space Complexity:
The space complexity of the algorithm is O(M) since in the worst case, the
whole pattern can have distinct characters which will go into the HashMap.
In the worst case, we also need O(N)O(N) space for the resulting substring,
which will happen when the input string is a permutation of the pattern.
"""


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        window_start, matched, substr_start = 0, 0, 0
        min_length = len(s) + 1
        char_frequency = {}

        for chr in t:
            if chr not in char_frequency:
                char_frequency[chr] = 0
            char_frequency[chr] += 1

        # try to extend the range [window_start, window_end]
        for window_end in range(len(s)):
            right_char = s[window_end]
            if right_char in char_frequency:
                char_frequency[right_char] -= 1
                if char_frequency[right_char] >= 0:  # Count every matching of a character
                    matched += 1

            # Shrink the window if we can, finish as soon as we remove a matched character
            while matched == len(t):
                if min_length > window_end - window_start + 1:
                    min_length = window_end - window_start + 1
                    substr_start = window_start

                left_char = s[window_start]
                window_start += 1
                if left_char in char_frequency:
                    # Note that we could have redundant matching characters, therefore we'll decrement the
                    # matched count only when a useful occurrence of a matched character is going out of the window
                    if char_frequency[left_char] == 0:
                        matched -= 1
                    char_frequency[left_char] += 1

        if min_length > len(s):
            return ""
        return s[substr_start:substr_start + min_length]
