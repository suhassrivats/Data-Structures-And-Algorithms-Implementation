def avg_of_subarrays_k(array, k):
    n = len(array)
    result = []

    for i in range(n-k):
        total = 0
        for j in range(i, i+k):
            total += array[j]
        result.append(total/k)
    print(result)
    return result

array = [1, 3, 2, 6, -1, 4, 1, 8, 2]
K=5
avg_of_subarrays_k(array, K)