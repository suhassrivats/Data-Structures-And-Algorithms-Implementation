class Solution:
    def reverseWords(self, s: str) -> str:
        words_list = s.split(' ')
        rev_words_list = [word[::-1] for word in words_list]
        return ' '.join(rev_words_list)
