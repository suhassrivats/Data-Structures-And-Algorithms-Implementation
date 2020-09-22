class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        """
        Complexity Analysis
            Let N be the number of characters in the input string and M be the
        number of characters in the banned list.

        Time Complexity: O(N+M)
            It would take O(N) time to process each stage of the pipeline as we
        built. In addition, we built a set out of the list of banned words,
        which would take O(M) time.
            Hence, the overall time complexity of the algorithm is O(N+M).

        Space Complexity: O(N+M)
            We built a hashmap to count the frequency of each unique word,
        whose space would be of O(N).
            Similarly, we built a set out of the banned word list, which would
        consume additional O(M) space.

        Therefore, the overall space complexity of the algorithm is O(N+M).
        """

        # 1) replace the punctuations with spaces,
        #      and put all letters in lower case
        normalized_str = ''.join([c.lower() if c.isalpha() else ' ' for c in paragraph])

        # 2) split the string into words
        words = normalized_str.split()
        banned_words = set(banned)
        word_frequency_count = {}

        # 3) count the appearance of each word, excluding the banned words
        for word in words:
            if word not in banned_words:
                word_frequency_count[word] = word_frequency_count.get(word, 0) + 1

        # 4) return the word with the highest frequency
        return max(word_frequency_count, key=word_frequency_count.get)
