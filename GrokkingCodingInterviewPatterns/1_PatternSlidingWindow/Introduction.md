# 1.0 Introduction

## Introduction

In many problems dealing with an array \(or a LinkedList\), we are asked to find or calculate something among all the contiguous subarrays \(or sublists\) of a given size. For example, take a look at this problem:

> Given an array, find the average of all contiguous subarrays of size ‘K’ in it.

Let’s understand this problem with a real input: `Array: [1, 3, 2, 6, -1, 4, 1, 8, 2], K=5` Here, we are asked to find the average of all contiguous subarrays of size ‘5’ in the given array. Let’s solve this:

`For the first 5 numbers (subarray from index 0-4), the average is: (1+3+2+6-1)/5 => 2.2(1+3+2+6−1)/5=>2.2` `The average of next 5 numbers (subarray from index 1-5) is: (3+2+6-1+4)/5 => 2.8(3+2+6−1+4)/5=>2.8` `For the next 5 numbers (subarray from index 2-6), the average is: (2+6-1+4+1)/5 => 2.4(2+6−1+4+1)/5=>2.4`

Here is the final output containing the averages of all contiguous subarrays of size 5: `Output: [2.2, 2.8, 2.4, 3.6, 2.8]`

A brute-force algorithm will calculate the sum of every 5-element contiguous subarray of the given array and divide the sum by ‘5’ to find the average. This is what the algorithm will look like:

```python
def find_averages_brute_force(K, arr):
    result = []

    for i in range(len(arr) - K + 1):
        window_sum = 0
        for j in range(i, i + K):
            window_sum += arr[j]
        result.append(window_sum / K)

    return result


# Example usage
arr = [1, 3, 2, 6, -1, 4, 1, 8, 2]
K = 5
print("Averages of subarrays of size K:", find_averages_brute_force(K, arr))
```

**Time complexity:** Since for every element of the input array, we are calculating the sum of its next ‘K’ elements, the time complexity of the above algorithm will be O\(N\*K\) where ‘N’ is the number of elements in the input array.

Can we find a better solution? Do you see any inefficiency in the above approach?

The inefficiency is that for any two consecutive subarrays of size ‘5’, the overlapping part \(which will contain four elements\) will be evaluated twice. For example, take the above-mentioned input:

![image](https://user-images.githubusercontent.com/20329508/113503322-c4ff8580-954e-11eb-8f7e-5fc6da8225ee.png)

As you can see, there are four overlapping elements between the subarray \(indexed from 0-4\) and the subarray \(indexed from 1-5\). Can we somehow reuse the sum we have calculated for the overlapping elements?

The efficient way to solve this problem would be to visualize each contiguous subarray as a sliding window of ‘5’ elements. This means that we will slide the window by one element when we move on to the next subarray. To reuse the sum from the previous subarray, we will subtract the element going out of the window and add the element now being included in the sliding window. This will save us from going through the whole subarray to find the sum and, as a result, the algorithm complexity will reduce to O\(N\).

![image](https://user-images.githubusercontent.com/20329508/113503352-f2e4ca00-954e-11eb-98a0-f496908131b3.png)

Here is the algorithm for the Sliding Window approach:

```python
def find_averages_sliding_window(K, arr):
    result = []
    window_sum = 0
    window_start = 0

    for window_end in range(len(arr)):
        window_sum += arr[window_end]  # add next element

        # slide the window when we hit size K
        if window_end >= K - 1:
            result.append(window_sum / K)  # calculate average
            window_sum -= arr[window_start]  # subtract element going out
            window_start += 1  # slide window forward

    return result


# Example usage
arr = [1, 3, 2, 6, -1, 4, 1, 8, 2]
K = 5
print("Averages of subarrays of size K:", find_averages_sliding_window(K, arr))
```

#### **Template to solve some sliding window problem:**

```python
from collections import defaultdict

def sliding_window_template(s, t):
    result = []
    if len(t) > len(s):
        return result

    # Build frequency map
    freq = defaultdict(int)
    for char in t:
        freq[char] += 1

    counter = len(freq)

    begin = 0
    end = 0

    while end < len(s):
        char = s[end]
        if char in freq:
            freq[char] -= 1
            if freq[char] == 0:
                counter -= 1

        end += 1

        # When condition is met (example: counter == 0)
        while counter == 0:
            # Save or update result here depending on problem
            result.append(s[begin:end])  # Example behavior

            temp_char = s[begin]
            if temp_char in freq:
                freq[temp_char] += 1
                if freq[temp_char] > 0:
                    counter += 1

            begin += 1

    return result
```
