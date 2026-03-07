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

Binary representation has 3 bits because N = 3.

```
bit 2   bit 1   bit 0
nums[2] nums[1] nums[0]
   3       2       1
```

| mask (decimal) | mask (binary) | j=0 calculation         | j=1 calculation         | j=2 calculation         | subset  |
| ---------- | ---------- | ----------------------- | ----------------------- | ----------------------- | ------- |
| 0          | 000        | 000 & 001 = 000 → skip  | 000 & 010 = 000 → skip  | 000 & 100 = 000 → skip  | []      |
| 1          | 001        | 001 & 001 = 001 → add 1 | 001 & 010 = 000 → skip  | 001 & 100 = 000 → skip  | [1]     |
| 2          | 010        | 010 & 001 = 000 → skip  | 010 & 010 = 010 → add 2 | 010 & 100 = 000 → skip  | [2]     |
| 3          | 011        | 011 & 001 = 001 → add 1 | 011 & 010 = 010 → add 2 | 011 & 100 = 000 → skip  | [1,2]   |
| 4          | 100        | 100 & 001 = 000 → skip  | 100 & 010 = 000 → skip  | 100 & 100 = 100 → add 3 | [3]     |
| 5          | 101        | 101 & 001 = 001 → add 1 | 101 & 010 = 000 → skip  | 101 & 100 = 100 → add 3 | [1,3]   |
| 6          | 110        | 110 & 001 = 000 → skip  | 110 & 010 = 010 → add 2 | 110 & 100 = 100 → add 3 | [2,3]   |
| 7          | 111        | 111 & 001 = 001 → add 1 | 111 & 010 = 010 → add 2 | 111 & 100 = 100 → add 3 | [1,2,3] |


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
