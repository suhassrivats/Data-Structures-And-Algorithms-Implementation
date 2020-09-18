class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        """
        Time Complexity:
            The time complexity of the above algorithm will be O(N * M * Len)
        where ‘N’ is the number of characters in the given string, ‘M’ is the
        total number of words, and ‘Len’ is the length of a word.

        Space Complexity:
            The space complexity of the algorithm is O(M) since at most, we
        will be storing all the words in the two HashMaps. In the worst case,
        we also need O(N) space for the resulting list. So, the overall space
        complexity of the algorithm will be O(M+N).
        """

        if len(words) == 0 or len(words[0]) == 0:
            return []
        word_frequency = {}

        # Keep the frequency of every word in a HashMap.
        for word in words:
            word_frequency[word] = word_frequency.get(word, 0) + 1

        result_indices = []
        words_count = len(words)
        word_length = len(words[0])
        words_total_length = words_count * word_length

        for i in range(len(s) - words_total_length+1):
            words_seen = {}
            for j in range(words_count):
                next_word_index = i + j * word_length
                # Get the next word from the string
                word = s[next_word_index:next_word_index+word_length]
                if word not in word_frequency:  # Break if we don't need this word
                    break
                # Add the word to the words_seen map
                words_seen[word] = words_seen.get(word, 0) + 1
                # No need to process further if the word has higher frequency than required
                if words_seen[word] > word_frequency.get(word, 0):
                    break
                if j+1 == words_count:
                    result_indices.append(i)

        return result_indices
