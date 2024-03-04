# Read about them here: https://www.scaler.com/topics/difference-between-subarray-subset-and-subsequence/

def generate_subarrays(array):
    n = len(array)
    for i in range(n):
        for j in range(i, n):
            for k in range(i, j+1):
                print(k, end=' ')
            print()

array = [1, 2, 3]
generate_subarrays(array)