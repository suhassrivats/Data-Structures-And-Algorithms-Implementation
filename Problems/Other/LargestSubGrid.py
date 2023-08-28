# https://leetcode.com/discuss/interview-question/850974/hackerrank-online-assessment-roblox-new-grad-how-to-solve-this

def largestSquareSubmatrix(arr, K):
    M = len(arr)
    N = len(arr[0])

    prefixSum = [[0] * (N + 1) for _ in range(M + 1)]

    for i in range(1, M + 1):
        for j in range(1, N + 1):
            prefixSum[i][j] = prefixSum[i - 1][j] + prefixSum[i][j - 1] - prefixSum[i - 1][j - 1] + arr[i - 1][j - 1]

    maxSize = 0

    for i in range(1, M + 1):
        for j in range(1, N + 1):
            for size in range(1, min(M - i + 2, N - j + 2)):
                sumSubmatrix = prefixSum[i + size - 1][j + size - 1] - prefixSum[i - 1][j + size - 1] - prefixSum[i + size - 1][j - 1] + prefixSum[i - 1][j - 1]
                if sumSubmatrix <= K:
                    maxSize = max(maxSize, size)

    return maxSize

# Example input
arr = [
    [1, 1, 1],
    [1, 1, 1],
    [1, 1, 1]
]
K = 4
print(largestSquareSubmatrix(arr, K))  # Output: 2
