### Find the Corrupt Pair (easy)

We are given an unsorted array containing ‘n’ numbers taken from the range 1 to ‘n’. The array originally contained all the numbers from 1 to ‘n’, but due to a data error, one of the numbers got duplicated which also resulted in one number going missing. Find both these numbers.

**Example 1:**

```
Input: [3, 1, 2, 5, 2]
Output: [2, 4]
Explanation: '2' is duplicated and '4' is missing.
```

**Example 2:**

```
Input: [3, 1, 2, 3, 6, 4]
Output: [3, 5]
Explanation: '3' is duplicated and '5' is missing.
```

### Solution 

This problem follows the **Cyclic Sort** pattern and shares similarities with [Find all Duplicate Numbers](https://www.educative.io/collection/page/5668639101419520/5671464854355968/5115834240335872/). Following a similar approach, we will place each number at its correct index. Once we are done with the cyclic sort, we will iterate through the array to find the number that is not at the correct index. Since only one number got corrupted, the number at the wrong index is the duplicated number and the index itself represents the missing number.