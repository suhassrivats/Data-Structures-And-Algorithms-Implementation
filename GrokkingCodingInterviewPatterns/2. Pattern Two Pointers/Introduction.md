# 2.1 Pair with Target Sum (easy)

Given an array of integers `nums` and an integer `target`, return **indices of the two numbers such that they add up to `target`.**

You may assume that each input would have **exactly one solution**, and you may not use the same element twice.

You can return the answer in any order.

---

## Example 1

```
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: nums[0] + nums[1] == 9
```

## Example 2

```
Input: nums = [3,2,4], target = 6
Output: [1,2]
```

## Example 3

```
Input: nums = [3,3], target = 6
Output: [0,1]
```

---

## Constraints

* `2 <= nums.length <= 10^4`
* `-10^9 <= nums[i] <= 10^9`
* `-10^9 <= target <= 10^9`
* **Only one valid answer exists**

---

## Follow-up

Can you design an algorithm better than **O(n²)** time complexity?

---

# Method 1: Brute Force

This approach checks every possible pair.

Total pairs = `n * (n - 1) / 2`

---

### Algorithm

1. Use one loop for the first index
2. Use a second loop for the second index
3. If sum equals target → return indices

---

### Python Implementation

```python
class Solution:
    def two_sum(self, nums, target):
        n = len(nums)

        for i in range(n - 1):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]

        return [-1, -1]
```

---

### Complexity Analysis

**Time Complexity:**
O(N²) — checking all pairs

**Space Complexity:**
O(1) — no extra space used

---

# Method 2: Using Sorting (Two Pointers)

If the array is sorted, we can use the two-pointer technique.

Since we must return original indices, we keep a copy.

---

### Algorithm

1. Copy the array
2. Sort the copy
3. Use two pointers:

   * Left → smallest
   * Right → largest
4. Compare sum with target:

   * If small → move left forward
   * If large → move right backward
5. Find original indices of the two values

---

### Python Implementation

```python
class Solution:
    def two_sum_sorting(self, nums, target):
        copy_nums = nums.copy()
        copy_nums.sort()

        left = 0
        right = len(copy_nums) - 1
        num1 = num2 = 0

        while left < right:
            s = copy_nums[left] + copy_nums[right]

            if s < target:
                left += 1
            elif s > target:
                right -= 1
            else:
                num1 = copy_nums[left]
                num2 = copy_nums[right]
                break

        # Find original indices
        result = []
        for i in range(len(nums)):
            if nums[i] == num1 and len(result) == 0:
                result.append(i)
            elif nums[i] == num2:
                result.append(i)

        return result
```

---

### Complexity Analysis

**Time Complexity:**
O(n log n) — due to sorting

**Space Complexity:**
O(n) — for the copied array

---

# Method 3: Using Hashing (Optimal Solution)

Instead of searching pairs, we search for the **complement**.

```
target - current_number = required_number
```

---

### Algorithm

1. Create a dictionary to store value → index
2. Traverse array
3. For each number:

   * Compute complement
   * If complement exists in map → solution found
   * Otherwise store current number

---

### Python Implementation

```python
class Solution:
    def two_sum_hashing(self, nums, target):

        hashmap = {}

        for i in range(len(nums)):
            complement = target - nums[i]

            if complement in hashmap:
                return [hashmap[complement], i]

            hashmap[nums[i]] = i

        raise ValueError("No two sum solution")
```

---

### Complexity Analysis

**Time Complexity:**
O(n) — single pass

**Space Complexity:**
O(n) — hashmap storage

---

# ✅ Summary of Approaches

| Method                 | Time Complexity | Space Complexity | Notes                        |
| ---------------------- | --------------- | ---------------- | ---------------------------- |
| Brute Force            | O(n²)           | O(1)             | Simple but slow              |
| Sorting + Two Pointers | O(n log n)      | O(n)             | Cannot modify original order |
| Hashing                | O(n)            | O(n)             | Optimal solution             |
