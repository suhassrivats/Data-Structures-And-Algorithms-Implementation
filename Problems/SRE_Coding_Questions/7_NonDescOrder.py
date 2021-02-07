'''
You are given a string. Rearrange characters of this string in non-ascending
order and output the resulting string.

The input data consists of a single string. The length of the string is between
1 and 50 characters, inclusive. Each character of the string is a lower-case
letter of English alphabet.

Example:
input
interview

output
wvtrniiee
'''
# This is Python 2
import sys


# Using sort funtion
def non_asc_order(s):
    """
    Time complexity: n*log(n) for sorting string, where n in the length of string/list
    Space Complexity (auxiliary): O(n), to store a list of strings of length n
    """
    s.sort(reverse=True)
    non_asc_string = ''.join(s)
    print(non_asc_string)
    return non_asc_string


def main():
    # Fetch input
    line = sys.stdin.readline()
    # Convert string to a list of characters
    s = list(line)
    non_asc_order(s)


if __name__ == '__main__':
    main()
