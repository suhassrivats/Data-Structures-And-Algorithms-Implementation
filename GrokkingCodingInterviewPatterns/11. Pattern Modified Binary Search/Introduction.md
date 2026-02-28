# Binary Search — Notes

## When to Use Binary Search

Use binary search when:

* The search space is **sorted** OR can be treated as monotonic
* You need to find:

  * Exact element
  * First/last occurrence
  * Boundary where condition changes (True/False)
  * Minimum/maximum feasible value
* Time complexity requirement is **O(log n)**

👉 Binary search is not just for arrays — it applies to **any monotonic (always increasing/decreasing/False->True transitions, etc) function**.

---

## Core Idea

Repeatedly divide the search space in half.

At each step:

1. Compute middle index
2. Compare with target (or condition)
3. Eliminate half of the space
4. Continue until bounds cross

---

## Standard Template (Exact Match)

```python
left, right = 0, len(nums) - 1

while left <= right:
    mid = left + (right - left) // 2
    
    if nums[mid] == target:
        return mid
    elif nums[mid] < target:
        left = mid + 1
    else:
        right = mid - 1

return -1
```

---

## Why `left + (right - left) // 2`?

Prevents integer overflow in languages like C++/Java.

---

## Two Major Binary Search Patterns

### 1) Search for Exact Value

Used when array is sorted and you need to find the element.

Examples:

* Classic binary search
* Search in rotated sorted array
* Find peak element

---

### 2) Search for Boundary (First/Last True)

Most interview problems use this pattern.

We search for the boundary where condition changes:

```
False False False True True True
                ↑ answer
```

---

## Lower Bound (First ≥ Target)

```python
left, right = 0, len(nums)

while left < right:
    mid = left + (right - left) // 2
    
    if nums[mid] < target:
        left = mid + 1
    else:
        right = mid

return left
```

---

## Upper Bound (First > Target)

```python
left, right = 0, len(nums)

while left < right:
    mid = left + (right - left) // 2
    
    if nums[mid] <= target:
        left = mid + 1
    else:
        right = mid

return left
```

---

## Binary Search on Answer (Very Important)

Search over **possible answers**, not indices.

Used when:

* Problem asks for minimum/maximum value
* You can check feasibility with a function
* Feasibility is monotonic

Pattern:

```python
left, right = min_possible, max_possible

while left < right:
    mid = left + (right - left) // 2
    
    if feasible(mid):
        right = mid
    else:
        left = mid + 1

return left
```

Examples:

* Capacity to ship packages
* Minimum eating speed
* Split array largest sum
* Allocate pages
* Aggressive cows

---

## Key Monotonic Patterns

Binary search works if condition behaves like:

* Increasing function
* Decreasing function
* False → True transition
* True → False transition

---

## Common Variations

### Search in Rotated Sorted Array

One half is always sorted — determine which half and discard the other.

---

### Find Peak Element

Use slope comparison:

* If nums[mid] < nums[mid+1] → peak on right
* Else → peak on left

---

### Infinite/Unknown Size Array

Increase right bound exponentially:

```python
right = 1
while arr[right] < target:
    right *= 2
```

---

## Loop Conditions

### `while left <= right`

* Used for exact search
* Ends when pointers cross

### `while left < right`

* Used for boundary search
* Prevents infinite loops
* Often paired with `right = mid`

---

## Complexity

Time: **O(log n)**
Space: **O(1)**

---

## Quick Mental Checklist

Ask yourself:

* Is the data sorted or monotonic?
* Am I searching index or answer space?
* Do I need exact match or boundary?
* Which template fits?
* What happens on duplicates?

