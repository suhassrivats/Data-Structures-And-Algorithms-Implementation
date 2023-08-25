from collections import defaultdict


class Solution:
    def countVowelSubstrings(self, word: str) -> int:
        # cuaieuouac
        vowels = set("aeiou")
        ans = left = start = 0
        window_vowels_counter = defaultdict(int)

        for right, ch in enumerate(word):
            if ch in vowels:
                window_vowels_counter[ch] += 1
                # Ensure that window_vowels_counter contains all 5 vowels
                if len(window_vowels_counter) < 5:
                    continue
                # If there are all vowels in dict, see if you can reduce the window size
                while window_vowels_counter[word[left]] > 1:
                    window_vowels_counter[word[left]] -= 1
                    left += 1
                # start is begining of the counter, left is end of counter
                # aeiou => length is 4 - 0 + 1. u->4pos a->0pos
                ans += left - start + 1
            else:
                window_vowels_counter.clear()
                # Reset the left and start pointers to the next character after the current one.
                left = start = right+1

        return ans