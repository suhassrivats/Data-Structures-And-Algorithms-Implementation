'''
A Fibonacci-like sequence is a sequence of integers a1, a2, ... for which
an = an-1+an-2 for all n > 2. You are given the first two elements of the
sequnce a1 and a2, and the 1-based index n. Output the n-th element of the
sequence.

The input data consists of a single line which contains integers a1, a2 and n
separated by single spaces. 0 < a1, a2, n < 10.

Example:
input
1 2 3

output
3
'''

import sys


def main():
    """
    Time Complexity: The time complexity of the iterative code is linear, as the
        loop runs from 2 to n, i.e. it runs in O(n) time
    Space Complexity: O(1), no auxiliary space required
    """
    line = sys.stdin.readline()
    a1, a2, n = line.strip().split(' ')
    a1, a2, n = int(a1), int(a2), int(n)

    for num in range(2, n):
        next = a1+a2
        a1 = a2
        a2 = next

    print(a2)
    return a2


if __name__ == '__main__':
    main()
