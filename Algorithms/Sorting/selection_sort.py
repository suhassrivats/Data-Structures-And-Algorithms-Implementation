'''
Selection Sort:
- It is a brute force algorithm
- Locate the smallest element and put in the first place
- Then select select the second smallest element and put it the
 second place. and so on..
- Final output ordering generated one by one in the sequence

Time Complexity Analysis:
- Two basic operation in sorting algorithms are comparision and swap.
- Comparision:
    First iteration: (n-1)
    Second: (n-2)
    Total comparisions: (n-1) + (n-2) + ... + 1 + 0 = n(n-1)/2

- Swap: For every iteration there is one swap.
    First iteration: 1
    Second iteration: 2*1
    nth iteration: n*1 = n

- Expression:
    Assume, a[j] < a[smallest] takes C5 constant time
    a[i], a[smallest] = a[smallest], a[i] takes C6 constant time
    increment i counter in for loop takes or other miscellanios stuff C7 time

    T(N) = [n(n+1)/2]*C5 + n*C6 + C7

    when n -> infinity

    T(N) = O(n^2) // Asymptotic complexity
'''


def selection_sort(a):

    # Traverse through all the elements in an array
    for i in range(len(a)-1):

        # Assume the first element is the smallest initially
        smallest = i

        # Find the min element in the remaining unsorted array
        for j in range(i+1, len(a)):
            if a[j] < a[smallest]:
                smallest = j

        # Swap the found min element with the first element
        a[i], a[smallest] = a[smallest], a[i]

    print(a)

    return a


a = [1, 6, 4, 7, 9]
selection_sort(a)
