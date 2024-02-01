class Solution:
    def longestWord(self, words: List[str]) -> str:
        visited = set()
        # We need to first add empty string. Otherwise we can't add first word based on our logic
        visited.add('')

        result = ''
        # This will make sure that the words are sorted in lexicographically
        words.sort()

        for word in words:
            # Check if this word except last char is in visited. If so, it means that a new word
            # can be formed with this character
            if word[:-1] in visited:
                visited.add(word)
                if len(word) > len(result):
                    result = word
        return result
