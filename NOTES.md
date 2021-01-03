# LeetCode Advice

Read this before doing LC:

- https://medium.com/@alimirio/before-you-start-solving-problems-on-leetcode-prep-work-9d65fc964c6f

How to approach leetcode problems:

- https://www.youtube.com/watch?v=GbyXxUDVeAo
- [Optimal Leetcode learning strategy? Struggle or exposure?](https://www.reddit.com/r/cscareerquestions/comments/6rsxbm/optimal_leetcode_learning_strategy_struggle_or/dl971lp/)

Consistent practice advice:
- https://leetcode.com/discuss/general-discussion/318537/consistent-practice-advice
- https://news.ycombinator.com/item?id=7930098

Getting good at LC:

- https://heidi-newton.com/blog/getting-good-at-leetcode

Strategy to use LC for Cracking Coding Interviews Effectively:

- https://www.youtube.com/watch?v=q15JgVVLXQg

Facebook:

- https://leetcode.com/discuss/general-discussion/675445/facebook-interview-experiences-all-combined-from-lc-till-date-07-jun-2020

CTCI to LC:

- https://leetcode.com/discuss/interview-question/256347/ctci-questions-lists

List of questions sorted by common patterns:

- https://leetcode.com/discuss/career/448285/List-of-questions-sorted-by-common-patterns

How to pick best questions for interviews in GFG and LC:

- https://www.youtube.com/watch?v=HYK5lpkKBPo

Google Interview questions list | Jan 2020 - Jun 2020:

- https://leetcode.com/discuss/general-discussion/726900/google-interview-questions-list-jan-2020-jun-2020


# Miscellaneous

[Complexity of Python Operations](https://www.ics.uci.edu/~pattis/ICS-33/lectures/complexitypython.txt)

Space Complexity:

- [Detailed Explanation](https://www.youtube.com/watch?v=yOb0BL-84h8)

- [Space Complexity of Algorithms - How to Calculate Space Complexity of Algorithms in Data Structures
](https://www.youtube.com/watch?v=yOb0BL-84h8)
- [Space complexity short definitions](https://www.geeksforgeeks.org/g-fact-86/)

The space complexity of an algorithm or a computer program is the amount of memory space required to solve an instance of the computational problem as a function of the size of the input.

Simple words : It is the memory required by an algorithm to execute a program and produce output. Similar to time complexity, Space complexity is often expressed asymptotically in big O notation, such as O(n), O(nlog(n)), O(n^2) etc., where n is the input size in units of bits needed to represent the input.

For any algorithm, memory is required for the following purposes:

1. To store program instructions.
2. To store constant values
3. To store variable values
4. And for few other things like function calls, jumping statements etc.

Auxiliary Space : is the temporary space (excluding the input size) allocated by your algorithm to solve the problem, with respect to input size.

Space complexity includes both Auxiliary space and space used by input.

​		=> `Space Complexity = Input Size + Auxiliary space`

Huffman coding:

- https://www.youtube.com/watch?v=iiGZ947Tcck
- https://medium.com/iecse-hashtag/huffman-coding-compression-basics-in-python-6653cdb4c476

Python Lambda:

- https://pybit.es/dict-ordering.html
- https://dbader.org/blog/python-lambda-functions

Python Generators:

- https://realpython.com/introduction-to-python-generators/

Python Type Hints:

- https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html#when-you-re-puzzled-or-when-things-are-complicated
- https://mypy.readthedocs.io/en/stable/getting_started.html

How to use Cracking The Coding Interview (CTCI) book:

- https://www.quora.com/How-useful-is-Cracking-the-Coding-Interview-book-while-appearing-for-technical-interviews-of-companies-like-Google-Facebook-Amazon-etc

CTCI vs EPI:

- https://www.reddit.com/r/cscareerquestions/comments/4xel2x/ctci_vs_epi/

Heaps:

- [Heap - Heap Sort - Heapify - Priority Queues](https://www.youtube.com/watch?v=HqPJF2L5h9U&t=1125s)

Heap Sort:

- Time complexity analysis:
  - http://www.cs.toronto.edu/~krueger/cscB63h/lectures/tut02.txt
- Introduction:
  - https://www.programiz.com/dsa/heap-sort
- Building MaxHeap time complexity is `O(n)`:
  - https://www.youtube.com/watch?v=XZ_Beap6Vo0
  - https://www.youtube.com/watch?v=HI97KDV23Ig

Tries:

- [Trying to Understand Tries](https://medium.com/basecs/trying-to-understand-tries-3ec6bede0014)

How to use GFG:

- https://www.youtube.com/watch?v=07QCAJYolaE

Trees:

- [When is it practical to use DFS vs BFS](https://stackoverflow.com/questions/3332947/when-is-it-practical-to-use-depth-first-search-dfs-vs-breadth-first-search-bf)

Inspiration:

- https://leetcode.com/discuss/interview-question/765743/6-months-of-hard-work-and-finally-offer-from-facebook
- https://leetcode.com/discuss/interview-experience/808191/google-l3-mountain-view-august-2020-offer

Recursion:

- [Master recursion - Coding Ninjas](https://www.youtube.com/watch?v=O7IkZN1kAFQ)

Iteration vs Recursion:

- https://medium.com/@williambdale/recursion-the-pros-and-cons-76d32d75973a
- https://medium.com/backticks-tildes/iteration-vs-recursion-c2017a483890#:~:text=The%20concept%20of%20Recursion%20and,a%20certain%20condition%20is%20met

BinarySearch:

- [Python - Powerful Ultimate Binary Search Template. Solved many problems](https://leetcode.com/discuss/general-discussion/786126/python-powerful-ultimate-binary-search-template-solved-many-problems)

Graphs:

- [Introduction](https://www.youtube.com/watch?v=gXgEDyodOJU)
- [Properties](https://www.youtube.com/watch?v=AfYqN3fGapc)

How to crack Amazon Coding Interview:

- https://medium.com/@rachit138/how-i-cleared-the-amazon-sde-2-interview-f82a33706ff4


# Object Oriented Programming in Python
- [Encapsulation, Data Abstraction, Polymorphism, Inheritance](https://www.python-course.eu/object_oriented_programming.php)
- [Public, Private and Protected](https://www.tutorialsteacher.com/python/private-and-protected-access-modifiers-in-python)


# Coding Patterns

**Sliding Window:**

In many problems dealing with an array (or a LinkedList or strings), we are asked to find or calculate something among all the contiguous subarrays (or sublists or substrings) of a given size. Sliding Window technique can be used in such cases.

- [Introduction to Sliding Window Algorithms](https://levelup.gitconnected.com/an-introduction-to-sliding-window-algorithms-5533c4fe1cc7)
- [How to Solve Sliding Window Problems](https://medium.com/outco/how-to-solve-sliding-window-problems-28d67601a66)

**Two Pointers:**

In problems where we deal with sorted arrays (or LinkedLists) and need to find a set of elements that fulfill certain constraints, the Two Pointers approach becomes quite useful. The set of elements could be a pair, a triplet or even a subarray.

- [Introduction to Two Pointer Technique](https://www.geeksforgeeks.org/two-pointers-technique/)
- [Two different approaches of using two-pointer technique](https://afteracademy.com/blog/what-is-the-two-pointer-technique)

**Fast & Slow Pointers:**

The Fast & Slow pointer approach, also known as the Hare & Tortoise algorithm, is a pointer algorithm that uses two pointers which move through the array (or sequence/LinkedList) at different speeds. This approach is quite useful when dealing with cyclic LinkedLists or arrays.

By moving at different speeds (say, in a cyclic LinkedList), the algorithm proves that the two pointers are bound to meet. The fast pointer should catch the slow pointer once both the pointers are in a cyclic loop.
