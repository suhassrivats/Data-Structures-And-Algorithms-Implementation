class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        char_freq_S = {}
        num_jewels = 0

        # Store characters and its frequencies in a dictionary
        for char in S:
            char_freq_S[char] = char_freq_S.get(char, 0) + 1

        # If a jewel exists in char_freq_S, then sum each jewel's frequencies
        for char in J:
            if char in char_freq_S:
                num_jewels += char_freq_S[char]

        return num_jewels
