# README: Difference Between Subarray, Subset, and Subsequence

## Introduction
An **array** is a linear collection of values stored at contiguous memory locations. Understanding the concepts of **subarray**, **subset**, and **subsequence** is crucial for solving array-related problems effectively. This document explains their definitions, differences, examples, and how to calculate the number of each for a given array.

---

## Key Points About Arrays
1. **Contiguous Memory:** Arrays occupy continuous memory locations.
2. **Indexing:** Index starts at 0 and goes up to (length of array - 1).
3. **Fixed Size:** The size of an array is fixed upon creation.
4. **Fast Access:** Elements are accessible using indices.

### Example Array:
Array: `arr = [56, 50, 34, 24, 12]`

For more details, refer to articles on arrays in data structures.

---

## Definitions and Examples

### Subarray
A **subarray** is a contiguous portion of the array.
- **Order:** The sequence of elements is preserved.
- **Size Range:** From 1 to the size of the array.

#### Example:
Array: `arr = [1, 2, 3]`

Possible subarrays:
- `[1]`
- `[2]`
- `[3]`
- `[1, 2]`
- `[2, 3]`
- `[1, 2, 3]`

**Formula for Subarrays:**
Number of subarrays = `n * (n + 1) / 2`

---

### Subset
A **subset** is any possible combination of elements from the array.
- **Order:** Not necessarily preserved.
- **Includes:** All possible combinations, including empty set.

#### Example:
Array: `arr = [1, 2, 3]`

Possible subsets:
- `[]`
- `[1]`
- `[2]`
- `[3]`
- `[1, 2]`
- `[1, 3]`
- `[2, 3]`
- `[1, 2, 3]`

**Formula for Subsets:**
Number of subsets = `2^n`

---

### Subsequence
A **subsequence** is a sequence derived by deleting some or no elements from the array while maintaining the order.
- **Order:** Preserved from the original array.
- **Contiguity:** Not required.

#### Example:
Array: `arr = [1, 2, 3, 4]`

Possible subsequences:
- `[1]`
- `[2]`
- `[3]`
- `[4]`
- `[1, 2]`
- `[2, 3]`
- `[1, 3]`
- `[1, 2, 3, 4]`

**Formula for Subsequences:**
Number of subsequences = `2^n`

---

## Key Differences
| **Aspect**      | **Subarray**       | **Subset**         | **Subsequence**   |
|-----------------|-------------------|-------------------|------------------|
| **Definition**  | Contiguous part of an array | Any combination of elements | Sequence derived by deleting some elements |
| **Contiguity**  | Required           | Not required       | Not required     |
| **Order**       | Preserved          | Not preserved      | Preserved        |
| **Formula**     | `n * (n + 1) / 2`  | `2^n`              | `2^n`            |

---

## Summary of Counts
Given an array of size `n`:
- **Subarrays:** `n * (n + 1) / 2`
- **Subsets:** `2^n`
- **Subsequences:** `2^n`

### Example (Array Size = 3):
- Subarrays: `6`
- Subsequences: `8`
- Subsets: `8`

