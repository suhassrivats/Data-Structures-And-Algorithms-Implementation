# Subset Pattern Using Bitmasking

Bitmasking is a technique used to generate all subsets of a set efficiently. It works by representing each subset as a **binary number (bitmask)**.

If a list contains **N elements**, each element has **two choices**:

* Include the element
* Exclude the element

Therefore, the total number of subsets is:

```
2^N
```

We can represent each subset using a binary number from:

```
0 → 2^N - 1
```

Each **bit position** in the mask represents whether the corresponding element is included.

---

# Example

```
nums = [1, 2, 3]
N = 3
```

Total subsets:

```
2^3 = 8
```

Bit positions map to array indices:

```
bit 0 → nums[0] → 1
bit 1 → nums[1] → 2
bit 2 → nums[2] → 3
```

---

# Subset Generation Code

```python
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        all_subsets = []
        N = len(nums)

        for mask in range(0, 1 << N):

            cur_set = []

            for j in range(N):

                if mask & (1 << j):
                    cur_set.append(nums[j])

            all_subsets.append(cur_set)

        return all_subsets
```

---

# How the Bitmask Works

The expression:

```
mask & (1 << j)
```

checks whether the **j-th bit is set**.

If the result is non-zero, we include `nums[j]` in the subset.

Example:

```
mask = 5
binary = 101
```

```
1 << 2 = 100
```

```
 101
&100
----
 100  → include nums[2]
```

---

# Walkthrough Table

For:

```
nums = [1,2,3]
```

| mask (decimal) | mask (binary) | j=0 check | j=1 check | j=2 check | subset  |
| -------------- | ------------- | --------- | --------- | --------- | ------- |
| 0              | 000           | skip      | skip      | skip      | []      |
| 1              | 001           | add 1     | skip      | skip      | [1]     |
| 2              | 010           | skip      | add 2     | skip      | [2]     |
| 3              | 011           | add 1     | add 2     | skip      | [1,2]   |
| 4              | 100           | skip      | skip      | add 3     | [3]     |
| 5              | 101           | add 1     | skip      | add 3     | [1,3]   |
| 6              | 110           | skip      | add 2     | add 3     | [2,3]   |
| 7              | 111           | add 1     | add 2     | add 3     | [1,2,3] |

---

# Mental Model

Think of the bitmask as a **switch panel**.

```
nums = [1,2,3]

switches:
1 2 3
```

Mask:

```
101
```

Meaning:

```
ON  OFF  ON
```

Subset:

```
[1,3]
```

---

# Time Complexity

Outer loop:

```
2^N
```

Inner loop:

```
N
```

Total complexity:

```
O(N * 2^N)
```

This is optimal because every subset must be generated.

---

# Bitmask Tricks

Check if bit is set

```
mask & (1 << i)
```

Set bit

```
mask | (1 << i)
```

Clear bit

```
mask & ~(1 << i)
```

Toggle bit

```
mask ^ (1 << i)
```
