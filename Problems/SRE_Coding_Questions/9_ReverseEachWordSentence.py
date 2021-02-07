'''
You are given an integer N, followed by N lines of input (1 <= N <= 100). Each
line of input contains one or several words separated with single spaces. Each
word is a sequence of letters of English alphabet containing between 1 and 10
characters, inclusive. The total number of words in the input is between 1 and
100, inclusive.

Your task is to reverse each word in each line of input, while preserving the
order of words in each line. The lines of your output should not have any
trailing or leading spaces.

Example:

input
3
RemoteIo is awesome
Candidates pass interview
best candidates are selected

output
oIetomeR si emosewa
setadidnaC ssap weivretni
tseb setadidnac era detceles
'''

import sys


def reverseWordSentence(sentence):
    # Split the sentence into list of words.
    words = sentence.strip().split(" ")

    # Reverse each word in a list
    rev_words = [word[::-1] for word in words]

    # Join reveresed words into a string
    rev_sentence = " ".join(rev_words)
    print(rev_sentence)
    return rev_sentence


def main():
    line = sys.stdin.readline()
    sentences = []
    for i in range(int(line)):
        sentence = sys.stdin.readline()
        sentences.append(sentence)

    for sentence in sentences:
        reverseWordSentence(sentence)


if __name__ == '__main__':
    main()
