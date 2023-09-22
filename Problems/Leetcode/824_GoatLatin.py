class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        vowels = ['a', 'e', 'i', 'o', 'u']
        words = sentence.split()
        word_counter = 0
        gl_words = []
        for word in words:
            word_counter += 1
            suffix = "ma" + "a" * word_counter
            if word[0].lower() not in vowels:
                word = word[1:] + word[0]
            word += suffix
            gl_words.append(word)
        return ' '.join(gl_words)