def avg_of_subarrays_k(array, k):
    n = len(array)
    result = []

    for i in range(n-k+1):
        total = 0
        for j in range(i, i+k):
            total += array[j]
        result.append(total/k)
    print(result)
    return result


def avg_of_subarrays_k_winsize(array, k):
    win_st = 0
    win_sum = 0
    n = len(array)
    result = []

    for win_end in range(n):
        win_sum += array[win_end]
        if win_end >= k-1:
            result.append(win_sum/k)
            win_sum -= array[win_st]
            win_st += 1
    print(result)
    return result


array = [1, 3, 2, 6, -1, 4, 1, 8, 2]
K=5
avg_of_subarrays_k(array, K)
avg_of_subarrays_k_winsize(array, K)