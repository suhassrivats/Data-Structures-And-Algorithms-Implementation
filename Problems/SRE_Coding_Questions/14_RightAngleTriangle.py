# Print right angle triangle in Python
# Python patterns tutorial: https://pynative.com/print-pattern-python-examples/

def main():
    rows = int(input('Please enter the number of rows: '))
    for r in range(rows):
        for c in range(r):
            """
            *
            * *
            * * *
            * * * *
            """
            # print('*', end=' ')

            """
            1
            2 2
            3 3 3
            4 4 4 4
            """
            # print(r, end=' ')

            """
            0
            0 1
            0 1 2
            0 1 2 3
            """
            print(c, end=' ')
        print(' ')


if __name__ == '__main__':
    main()
