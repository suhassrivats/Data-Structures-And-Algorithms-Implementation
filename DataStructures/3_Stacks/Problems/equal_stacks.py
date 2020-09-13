"""
You have three stacks of cylinders where each cylinder has the same diameter, but they may vary in height. You can change the height of a stack by removing and discarding its topmost cylinder any number of times.

Find the maximum possible height of the stacks such that all of the stacks are exactly the same height. This means you must remove zero or more cylinders from the top of zero or more of the three stacks until they're all the same height, then print the height. The removals must be performed in such a way as to maximize the height.

Note: An empty stack is still a stack.

Input Format

The first line contains three space-separated integers, , , and , describing the respective number of cylinders in stacks , , and . The subsequent lines describe the respective heights of each cylinder in a stack from top to bottom:

The second line contains  space-separated integers describing the cylinder heights in stack . The first element is the top of the stack.
The third line contains  space-separated integers describing the cylinder heights in stack . The first element is the top of the stack.
The fourth line contains  space-separated integers describing the cylinder heights in stack . The first element is the top of the stack.
Constraints

Output Format

Print a single integer denoting the maximum height at which all stacks will be of equal height.

Sample Input

5 3 4
3 2 1 1 1
4 3 2
1 1 4 1
Sample Output

5

"""
#!/bin/python3

import os
import sys


def equalStacks(h1, h2, h3):
    h1 = h1[::-1]
    h2 = h2[::-1]
    h3 = h3[::-1]
    # Sum of all stacks
    sum_h1 = sum(h1)
    sum_h2 = sum(h2)
    sum_h3 = sum(h3)

    while not (sum_h1 == sum_h2 and sum_h2 == sum_h3):
        if (sum_h1 > sum_h2 or sum_h1 > sum_h3):
            t = h1.pop()
            sum_h1 -= t
        if (sum_h2 > sum_h1 or sum_h2 > sum_h3):
            t = h2.pop()
            sum_h2 -= t
        if (sum_h3 > sum_h1 or sum_h3 > sum_h2):
            t = h3.pop()
            sum_h3 -= t
    return sum_h1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n1N2N3 = input().split()

    n1 = int(n1N2N3[0])

    n2 = int(n1N2N3[1])

    n3 = int(n1N2N3[2])

    h1 = list(map(int, input().rstrip().split()))

    h2 = list(map(int, input().rstrip().split()))

    h3 = list(map(int, input().rstrip().split()))

    result = equalStacks(h1, h2, h3)

    fptr.write(str(result) + '\n')

    fptr.close()
