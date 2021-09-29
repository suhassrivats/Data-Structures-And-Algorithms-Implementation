"""
Given an array of integers, if there is the even index, double it, at the end,
it is equal to some value, then the array is valid.
"""


def main():
    input = [3, 6, 12, 1, 5, 8]
    for i, num in enumerate(input):
        if i % 2 == 0:
            print(i, num)
            input[i] = 2 * num
    print(input)
    return input


if __name__ == '__main__':
    main()
