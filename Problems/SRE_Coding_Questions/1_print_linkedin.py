'''
Write a program which prints out all numbers between 1 and
100. When the program would print out a number exactly
divisible by 4, print "Linked" instead. When it would print
 out a number exactly divisible by 6, print "In" instead.
 When it would print out a number exactly divisible by both
 4 and 6, print "LinkedIn."
'''

#!/usr/bin/python


def print_linkedin():
    """
    Time Complexity: O(n) where n is the range. Since n=100 (constant) in this
        case, we can argue that complexity is O(1)
    Space Complexity: O(1)
    """

    for i in range(1, 101):
        # LCM of 4,6 is 12
        # if i % 12 == 0:
        if i % 4 == 0 and i % 6 == 0:
            print('LinkedIn')
        elif i % 4 == 0:
            print('Linked')
        elif i % 6 == 0:
            print('In')
        else:
            print(i)


if __name__ == '__main__':
    print_linkedin()
