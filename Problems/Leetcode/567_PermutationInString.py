class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        """
        Intuition:
        This problem follows the Sliding Window pattern, and we can use a similar 
        sliding window strategy as discussed in Longest Substring with K Distinct 
        Characters. We can use a HashMap to remember the frequencies of all 
        characters in the given pattern. Our goal will be to match all the 
        characters from this HashMap with a sliding window in the given string. 
        Here are the steps of our algorithm:

        - Create a HashMap to calculate frequencies of all characters in the pattern.
        - Iterate through the string, adding one character at a time in the sliding 
        window.
        - If the character being added matches a character in the HashMap, decrement 
        its frequency in the map. If the character frequency becomes zero, we got a 
        complete match.
        - If at any time, the number of characters matched is equal to the number of 
        distinct characters in the pattern (i.e., total characters in the HashMap), 
        we have gotten our required permutation.
        - If the window size is greater than the length of the pattern, shrink the 
        window to make it equal to the pattern’s size. At the same time, if the 
        character going out was part of pattern, put it back in the frequency HashMap

        Time Complexity:
        The above algorithm’s time complexity will be O(N + M), where ‘N’ and ‘M’ are 
        the number of characters in the input string and the pattern, respectively.

        Space Complexity:
        The algorithm’s space complexity is O(M) since, in the worst case, the whole 
        pattern can have distinct characters that will go into the HashMap.
        """
        
        pattern = s1
        string = s2

        window_start, matched = 0, 0
        char_frequency = {}

        for chr in pattern:
            char_frequency[chr] = char_frequency.get(chr, 0) + 1

        # our goal is to match all the characters from the 'char_frequency' with the current window
        # try to extend the range [window_start, window_end]
        for window_end in range(len(string)):
            right_char = string[window_end]
            if right_char in char_frequency:
                # decrement the frequency of matched character
                char_frequency[right_char] -= 1
                if char_frequency[right_char] == 0:
                    matched += 1

            if matched == len(char_frequency):
                return True

            # shrink the window by one character
            if window_end >= len(pattern) - 1:
                left_char = string[window_start]
                window_start += 1
                if left_char in char_frequency:
                    if char_frequency[left_char] == 0:
                        matched -= 1
                    char_frequency[left_char] += 1

        return False
